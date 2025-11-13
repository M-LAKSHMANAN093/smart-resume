from django import forms
from .models import Profile, Education, Skill, Project

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["phone", "photo", "summary"]
        widgets = {
            "summary": forms.Textarea(attrs={"rows": 4}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["institution", "degree", "start_year", "end_year"]

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["name", "level"]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "link"]
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}
