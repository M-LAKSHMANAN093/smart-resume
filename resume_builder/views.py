from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Education, Skill, Project
from .forms import ProfileForm, EducationForm, SkillForm, ProjectForm
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO

def home(request):
    if request.user.is_authenticated:
        return redirect("resume:preview")
    return render(request, "resume_builder/home.html")

@login_required
def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    EducationFormSet = modelformset_factory(Education, form=EducationForm, extra=1, can_delete=True)
    SkillFormSet = modelformset_factory(Skill, form=SkillForm, extra=1, can_delete=True)
    ProjectFormSet = modelformset_factory(Project, form=ProjectForm, extra=1, can_delete=True)

    if request.method == "POST":
        p_form = ProfileForm(request.POST, request.FILES, instance=profile)
        edu_formset = EducationFormSet(request.POST, prefix="edu", queryset=profile.educations.all())
        skill_formset = SkillFormSet(request.POST, prefix="skill", queryset=profile.skills.all())
        proj_formset = ProjectFormSet(request.POST, prefix="proj", queryset=profile.projects.all())

        if p_form.is_valid() and edu_formset.is_valid() and skill_formset.is_valid() and proj_formset.is_valid():
            p_form.save()
            # save formsets
            for f in edu_formset:
                if f.cleaned_data and not f.cleaned_data.get("DELETE", False):
                    obj = f.save(commit=False)
                    obj.profile = profile
                    obj.save()
                elif f.cleaned_data.get("DELETE", False) and f.instance.pk:
                    f.instance.delete()

            for f in skill_formset:
                if f.cleaned_data and not f.cleaned_data.get("DELETE", False):
                    obj = f.save(commit=False)
                    obj.profile = profile
                    obj.save()
                elif f.cleaned_data.get("DELETE", False) and f.instance.pk:
                    f.instance.delete()

            for f in proj_formset:
                if f.cleaned_data and not f.cleaned_data.get("DELETE", False):
                    obj = f.save(commit=False)
                    obj.profile = profile
                    obj.save()
                elif f.cleaned_data.get("DELETE", False) and f.instance.pk:
                    f.instance.delete()

            return redirect("resume:preview")
    else:
        p_form = ProfileForm(instance=profile)
        edu_formset = EducationFormSet(prefix="edu", queryset=profile.educations.all())
        skill_formset = SkillFormSet(prefix="skill", queryset=profile.skills.all())
        proj_formset = ProjectFormSet(prefix="proj", queryset=profile.projects.all())

    context = {
        "p_form": p_form,
        "edu_formset": edu_formset,
        "skill_formset": skill_formset,
        "proj_formset": proj_formset,
    }
    return render(request, "resume_builder/edit_profile.html", context)

@login_required
def preview_resume(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, "resume_builder/preview.html", {"profile": profile})

@login_required
def download_pdf(request):
    profile = get_object_or_404(Profile, user=request.user)
    html = render_to_string("resume_builder/pdf_template.html", {"profile": profile, "user": request.user})
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{request.user.username}_resume.pdf"'
        return response
    return HttpResponse("Error generating PDF", status=500)
