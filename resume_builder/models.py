from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to="profiles/", blank=True, null=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="educations")
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} @ {self.institution}"

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=3)  # 1-5

    def __str__(self):
        return f"{self.name} ({self.level})"

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
