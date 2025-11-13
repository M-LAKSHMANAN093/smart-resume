from django.urls import path
from . import views

app_name = "technical_test"

urlpatterns = [
    path("", views.choose_category, name="categories"),
    path("start/<str:category>/", views.start_test, name="start_test"),
]
