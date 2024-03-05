from django.db.models import Sum
from unapausa.models import Emotions, EmotionsLog
from django.utils import timezone
from datetime import timedelta

# Importa las funciones necesarias de Django
from django.utils import timezone
from django.db.models import Sum

# Función para obtener el promedio de emociones del usuario en la última semana
def get_emotion_average(user):
    # Obtiene la fecha y hora actuales
    now = timezone.now()
    # Calcula la fecha y hora de hace una semana
    week_ago = now - timedelta(days=7)

    # Filtra los registros de emociones del usuario en la última semana
    logs = EmotionsLog.objects.filter(user=user, date_joined__gte=week_ago)

    # Calcula el total de recuentos de emociones en la última semana
    total_count = logs.aggregate(total=Sum('count'))['total']

    # Obtiene el recuento de cada emoción y su porcentaje en el total
    emotion_counts = logs.values('emotion').annotate(count=Sum('count'))

    # Inicializa diccionarios para almacenar porcentajes de emociones y mensajes de alerta
    emotion_percentages = {}
    alert_messages = {}

    # Itera sobre los recuentos de emociones
    for emotion_count in emotion_counts:
        # Obtiene la instancia de la emoción correspondiente
        emotion = Emotions.objects.get(id=emotion_count['emotion'])
        
        # Calcula el porcentaje de esa emoción en el total
        percentage = int((emotion_count['count'] / total_count) * 100)
        emotion_percentages[emotion.name] = percentage

        # Verifica si el porcentaje es mayor o igual al 50% y si la emoción es de interés
        if percentage >= 50 and emotion.name in ["Tristeza", "Miedo", "Ira", "Calma", "Alegria"]:
            # Obtiene un mensaje de alerta personalizado
            alert_messages[emotion.name] = get_alert_message(emotion.name)

    # Retorna un diccionario con los porcentajes y mensajes de alerta
    return {"emotion_percentages": emotion_percentages, "alert_messages": alert_messages}

# Función para obtener un mensaje de alerta personalizado para una emoción dada
def get_alert_message(emotion):
    # Plantilla base para el mensaje
    message_template = f"Hemos notado que has seleccionado {emotion} en más del 50% de tus registros."

    # Verifica el tipo de emoción y construye un mensaje personalizado
    if emotion in ["Tristeza", "Miedo", "Ira"]:
        return f"{message_template} Si necesitas hablar con alguien, no dudes en contactarnos. Te dejaremos algunos enlaces que pueden ser de ayuda: ejemplo: [Enlace 1] ejemplo: [Enlace 2]"
    elif emotion in ["Calma", "Alegria"]:
        return f"{message_template} Nos alegra saber que te sientes bien. Esperamos que sigas así."
    else:
        return f"Esperamos que sigas con ese equilibrio emocional."

# Crea un diccionario de mensajes de alerta personalizados para ciertas emociones
custom_messages = {emotion: get_alert_message(emotion) for emotion in ["Tristeza", "Miedo", "Ira"]}
