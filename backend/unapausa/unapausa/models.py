from django.db import models
from django.contrib.auth.models import User


class Emotions(models.Model):
    name = models.CharField(max_length=15)
    img_emotion = models.ImageField(upload_to="files/staticfiles/emotions")

    def __str__(self):
        return self.name


class EmotionsLog(models.Model):
    # Relacion de uno a muchos hecha automaticamente al crear el obj ForeignKey.
    # on_delete=models.CASCADE significa que si el usuario es borrado del sistema, sus datos en esta tabla tambien se borraran.
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateField(unique=True)
    id_emotion = models.ForeignKey(Emotions, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.id_emotion.name}/ Date: {self.date_joined} "


class HealthyHabit(models.Model):
    habit_name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def __str__(self):
        return self.habit_name


class CheckList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    habit_id = models.ForeignKey(HealthyHabit, on_delete=models.CASCADE)
    date_joined = models.DateField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"habit: {self.habit_id.habit_name}/ date: {self.date_joined}/ is_done: {self.is_done}"
