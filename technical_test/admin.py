from django.contrib import admin
from .models import Question, Choice, TestSession

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "category", "difficulty")
    inlines = [ChoiceInline]

@admin.register(TestSession)
class TestSessionAdmin(admin.ModelAdmin):
    list_display = ("user", "started_at", "finished_at", "score")
