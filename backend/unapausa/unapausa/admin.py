from django.contrib import admin
from .models import CheckList, Emociones, RegistroDeEmociones, User



admin.site.register([
    CheckList, 
    Emociones, 
    RegistroDeEmociones, 
    User
])
