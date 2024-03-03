from django.urls import path, re_path
from . import views

urlpatterns = [
    path("habits/", views.get_habits, name="get_habits"),
    path("habits/<int:id>/", views.user_habits, name="user_habits"),
]
