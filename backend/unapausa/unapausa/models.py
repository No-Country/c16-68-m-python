from django.db import models
from django.contrib.auth.models import User


class Emotions(models.Model):
    # TODO: saber si usaremos un campo de imagen ya que asi esta en el diagrama, si es si, implementarlo.
    name = models.CharField(max_length=15)
    img_emotion = models.ImageField(upload_to="files/staticfiles/emotions")

    def __str__(self):
        return self.name


class EmotionsLog(models.Model):
    # TODO: creo que hay un bug en ManyTomanyField.
    # Relacion de uno a muchos hecha automaticamente al crear el obj ForeignKey.
    # on_delete=models.CASCADE significa que si el usuario es borrado del sistema, sus datos en esta tabla tambien se borraran.
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateField(unique=True)
    id_emotion = models.ForeignKey(Emotions, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"user_id: {self.user_id}\n id_emotion: {self.id_emotion} date: {self.date_joined} "


class HealthyHabit(models.Model):
    habit_name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def __str__(self):
        return f"habit: {self.habit}"


class CheckList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    habit_id = models.ForeignKey(HealthyHabit, on_delete=models.CASCADE)
    date_joined = models.DateField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"user_id: {self.user_id} habit: {self.habit} date: {self.date_joined}"
