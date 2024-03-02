from django.contrib import admin
from .models import CheckList, HealthyHabit, Emotions, EmotionsLog, User


admin.site.register([CheckList, HealthyHabit, Emotions, EmotionsLog, User])
