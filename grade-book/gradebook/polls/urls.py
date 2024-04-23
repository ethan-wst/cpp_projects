from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:course_number>/", views.course, name = "course"),
]