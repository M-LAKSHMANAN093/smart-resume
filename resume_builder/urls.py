from django.urls import path
from . import views

app_name = "resume"

urlpatterns = [
    path("", views.home, name="home"),
    path("edit/", views.edit_profile, name="edit"),
    path("preview/", views.preview_resume, name="preview"),
    path("download/", views.download_pdf, name="download_pdf"),
    path("education/delete/<int:edu_id>/", views.delete_education, name="delete_education"),

]
