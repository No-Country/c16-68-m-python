from django.db.models import Sum
from unapausa.models import Emotions, EmotionsLog
from django.utils import timezone
from datetime import timedelta

def get_emotion_average(user):
    now = timezone.now()
    week_ago = now - timedelta(days=7)
    logs = EmotionsLog.objects.filter(user=user, date_joined__gte=week_ago)
    total_count = logs.aggregate(total=Sum('count'))['total']

    emotion_counts = logs.values('emotion').annotate(count=Sum('count'))

    emotion_percentages = {}
    alert_messages = {}
    for emotion_count in emotion_counts:
        emotion = Emotions.objects.get(id=emotion_count['emotion'])
        percentage = int((emotion_count['count'] / total_count) * 100)
        emotion_percentages[emotion.name] = percentage

        if percentage >= 50 and emotion.name in ["Tristeza", "Miedo", "Ira", "Calma", "Alegria"]:
            alert_messages[emotion.name] = get_alert_message(emotion.name)

    return {"emotion_percentages": emotion_percentages, "alert_messages": alert_messages}

def get_alert_message(emotion):
    message_template = f"Hemos notado que has seleccionado {emotion} en más del 50% de tus registros."

    if emotion in ["Tristeza", "Miedo", "Ira"]:
        return f"{message_template} Si necesitas hablar con alguien, no dudes en contactarnos. Te dejaremos algunos enlaces que pueden ser de ayuda: ejemplo: [Enlace 1] ejemplo: [Enlace 2]"
    elif emotion in ["Calma", "Alegria"]:
        return f"{message_template} Nos alegra saber que te sientes bien. Esperamos que sigas así."
    else:
        return f"Esperamos que sigas con ese equilibrio emocional."

custom_messages = {emotion: get_alert_message(emotion) for emotion in ["Tristeza", "Miedo", "Ira"]}