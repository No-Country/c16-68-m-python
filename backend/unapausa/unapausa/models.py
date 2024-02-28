from django.db import models
from django.contrib.auth.models import User


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


class Healthy_Habit(models.Model):
    habit = models.CharField(max_length=50)

    def __str__(self):
        return f"habit: {self.habit}"


class CheckList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    habit = models.ForeignKey(Healthy_Habit, on_delete=models.CASCADE)
    date_joined = models.DateField()
    is_done = models.BooleanField(default=False)
    description = models.TextField(null=True)

    def __str__(self):
        return f"user_id: {self.user_id} habit: {self.habit} date: {self.date_joined}"
