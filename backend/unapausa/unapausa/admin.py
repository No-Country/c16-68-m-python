from django.contrib import admin
from .models import CheckList, Healthy_Habit, Emociones, RegistroDeEmociones


admin.site.register([CheckList, Healthy_Habit, Emociones, RegistroDeEmociones])
