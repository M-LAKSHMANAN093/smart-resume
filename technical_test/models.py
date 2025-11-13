from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Question(models.Model):
    CATEGORY_CHOICES = [("python","Python"),("sql","SQL"),("django","Django")]
    text = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    difficulty = models.IntegerField(default=3)

    def __str__(self):
        return self.text[:50]

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=400)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:60]

class TestSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.started_at}"
