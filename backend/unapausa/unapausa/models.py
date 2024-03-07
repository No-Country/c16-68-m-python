from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being true")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being true")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):

    email = models.EmailField(max_length=80, unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        text = "{0}    {1}"
        return text.format(self.email, self.username)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}


class Emotions(models.Model):

    EMOTIONS = [
        ("Tristeza", "Tristeza"),
        ("Miedo", "Miedo"),
        ("Ira", "Ira"),
        ("Sorpresa", "Sorpresa"),
        ("Alegria", "Alegria"),
        ("Amor","Amor")
    ]

    name = models.CharField(max_length=15, choices=EMOTIONS)
    # se ignorara el campo de imagenes ya que se habia hablado que las imagenes las guarde el front
    img_emotion = models.ImageField(upload_to="emotions", null=False)

    def __str__(self):
        return self.name

    """ @classmethod
    def initialize_emotions(cls):
        for emotion_name, _ in cls.EMOTIONS:
            cls.objects.get_or_create(name=emotion_name) """

class EmotionsLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    date_joined = models.DateField(auto_now_add=True)
    emotion = models.ForeignKey(Emotions, on_delete=models.CASCADE)
    description = models.TextField()
    count = models.IntegerField(default=1)

    class Meta:
        unique_together = ('user', 'emotion')

    def __str__(self):
        return f"{self.emotion.name}/ Date: {self.date_joined} "


class HealthyHabit(models.Model):
    habit_name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def __str__(self):
        return self.habit_name


class CheckList(models.Model):
    user_id = models.ForeignKey("unapausa.User", on_delete=models.CASCADE)
    habit_id = models.ForeignKey(HealthyHabit, on_delete=models.CASCADE)
    date_joined = models.DateField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"habit: {self.habit_id.habit_name}/ date: {self.date_joined}/ is_done: {self.is_done}"
