from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from unapausa.models import Emotions, EmotionsLog
from .serializers import EmotionSerializer, EmotionLogSerializer
from rest_framework import permissions, status
from .utils import get_emotion_average

# pendiente: formatear las emociones a minuscúlas siempre (hablar con el front si van a usar img o formularios)

class EmotionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        emotions = Emotions.objects.all()
        serializer = EmotionSerializer(emotions, many=True)
        emotion_average = get_emotion_average(request.user)
        return Response({"emotions": serializer.data, "emotion_average": emotion_average}, status=status.HTTP_200_OK)

class EmotionLogView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user_id = request.user.id
        emotion_name = request.data.get("emotion")
        description = request.data.get("description")

        # Verifica si la emoción proporcionada está en la lista de emociones permitidas
        allowed_emotions = [emotion[0] for emotion in Emotions.EMOTIONS]
        if emotion_name not in allowed_emotions:
            return Response({"message": "Invalid emotion"}, status=status.HTTP_400_BAD_REQUEST)

        # Obtiene la instancia del usuario
        User = get_user_model()
        user = User.objects.get(id=user_id)

        # Obtiene la emoción
        emotion, created = Emotions.objects.get_or_create(name=emotion_name)

        # Intenta obtener el registro de emoción para el usuario, o crea uno nuevo si no existe
        emotion_log, created = EmotionsLog.objects.get_or_create(user=user, emotion=emotion, defaults={'count': 0})

        # Incrementa el contador de la emoción
        emotion_log.count += 1
        emotion_log.description = description
        emotion_log.save()

        return Response({"message": "Emotion log updated successfully"}, status=status.HTTP_200_OK)

    def get(self, request, user_id=None):
        # validamos que se pase un id de usuario
        if user_id is None:
            user_id = request.user.id
        # Obtiene todos los registros de emociones del usuario
        emotion_logs = EmotionsLog.objects.filter(user_id=user_id)
        serializer = EmotionLogSerializer(emotion_logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, log_id=None):
        # validamos que se pase un id de registro
        if log_id is None:
            return Response({"message": "Log ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Obtiene el registro de emociones específico
        try:
            emotion_log = EmotionsLog.objects.get(id=log_id, user=request.user)
        except EmotionsLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Actualiza la descripción del registro de emociones
        description = request.data.get("description")
        if description is not None:
            emotion_log.description = description
            emotion_log.save()

        serializer = EmotionLogSerializer(emotion_log)
        return Response(serializer.data, status=status.HTTP_200_OK)