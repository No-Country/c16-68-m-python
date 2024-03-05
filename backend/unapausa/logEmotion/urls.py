from django.urls import path
from . import views

urlpatterns = [
    path("emotions/", views.EmotionView.as_view(), name="get-emotions"),
    path("emotion_logs/", views.EmotionLogView.as_view(), name="log-emotion"),
    path("emotion_logs/<int:user_id>/", views.EmotionLogView.as_view(), name="get-emotion-logs"),
    path("update_log/<int:log_id>/", views.EmotionLogView.as_view(), name="update-emotion-log"),
]