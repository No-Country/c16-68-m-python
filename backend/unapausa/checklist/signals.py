from django.db.models.signals import post_migrate
from django.dispatch import receiver
from unapausa.models import HealthyHabit

habits = [
    "Leer, La lectura estimula la mente, reduce el estrés, fomenta la empatía y promueve la creatividad siendo estos grandes beneficios para el bienestar general.",
    "Establecimiento de metas,Definir metas proporciona un propósito claro, motivación y satisfacción, elementos fundamentales para el desarrollo personal y el bienestar emocional.",
    "Tiempo al aire libre, Conectar con la naturaleza alivia tensiones, aumenta la vitamina D y mejora el bienestar emocional, siendo esencial para el equilibrio mental.",
    "Sueño de calidad, Un descanso reparador fortalece la mente, mejorando la memoria, la concentración y reduce la irritabilidad, facilitando enfrentar los desafíos diarios.",
    "Alimentación balanceada, Una dieta equilibrada proporciona nutrientes esenciales para el óptimo funcionamiento cerebral, influyendo positivamente en el ánimo y la claridad mental.",
    "Ejercicio regular, La actividad física habitual libera endorfinas, alivia el estrés, eleva el estado de ánimo y contribuye a una salud física integral, generando bienestar general.",
    "Meditación diaria, Cultivar la meditación diaria fomenta la serenidad mental, reduce el estrés y mejora la concentración, brindando equilibrio y bienestar.",
]


@receiver(post_migrate)
def populate_habit_table(sender, **kwargs):
    print("SENAL POSTMIGRATEE")
    if sender.name == "checklist":
        if not HealthyHabit.objects.exists():
            for habit in habits:
                HealthyHabit.objects.create(
                    habit_name=habit.split(",")[0].strip(),
                    description=habit.split(",")[1].strip(),
                )
