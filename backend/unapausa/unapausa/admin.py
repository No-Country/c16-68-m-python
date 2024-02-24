from django.contrib import admin
from .models import CheckList, Emociones, RegistroDeEmociones


admin.site.register([CheckList, Emociones, RegistroDeEmociones])
