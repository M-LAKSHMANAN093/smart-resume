from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, Choice, TestSession
from django.utils import timezone

@login_required
def start_test(request, category="python"):
    # simple test: fetch 5 questions from category
    qs = Question.objects.filter(category=category)[:5]
    if request.method == "POST":
        total = 0
        for q in qs:
            ans = request.POST.get(str(q.id))
            if ans:
                choice = Choice.objects.filter(id=int(ans)).first()
                if choice and choice.is_correct:
                    total += 1
        ts = TestSession.objects.create(user=request.user, finished_at=timezone.now(), score=total)
        return render(request, "technical_test/result.html", {"score": total, "total": qs.count()})
    return render(request, "technical_test/start.html", {"questions": qs, "category": category})

@login_required
def choose_category(request):
    return render(request, "technical_test/categories.html")
