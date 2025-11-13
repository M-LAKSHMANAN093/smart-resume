from django.contrib import admin
from .models import Profile, Education, Skill, Project

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone")

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("profile", "institution", "degree", "start_year", "end_year")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("profile", "name", "level")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("profile", "title")
