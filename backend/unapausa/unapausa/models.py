from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        email= self.normalize_email(email)

        user = self.model(
            email= email,
            **extra_fields
        )
        
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser has to have is_staff being true')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser has to have is_superuser being true')

        return self.create_user(email=email, password=password, **extra_fields)



class User(AbstractUser):

    email = models.EmailField(max_length=80, unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        text = '{0}    {1}'
        return text.format(self.email, self.username)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }







class Emociones(models.Model):
    # TODO: saber si usaremos un campo de imagen ya que asi esta en el diagrama, si es si, implementarlo.
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    # No se si se va a agregar una imagen de la emocion en la base de datos

    def __str__(self):
        return self.name


class RegistroDeEmociones(models.Model):
    # TODO: creo que hay un bug en ManyTomanyField.
    # Relacion de uno a muchos hecha automaticamente al crear el obj ForeignKey.
    # on_delete=models.CASCADE significa que si el usuario es borrado del sistema, sus datos en esta tabla tambien se borraran.
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateField(unique=True)
    id_emotion = models.ManyToManyField(Emociones)
    description = models.TextField()

    def __str__(self):
        return f"user_id: {self.user_id} id_emotion: {self.id_emotion} date: {self.date_joined} "


class CheckList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=35)
    date_joined = models.DateField()

    def __str__(self):
        return f"user_id: {self.user_id} activity_name: {self.activity_name} date: {self.date_joined}"
