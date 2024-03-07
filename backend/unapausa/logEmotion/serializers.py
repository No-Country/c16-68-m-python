from unapausa.models import User, Emotions, EmotionsLog
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotions
        fields = ['name','img_emotion']

class EmotionLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    emotion = EmotionSerializer(read_only=True)

    class Meta:
        model = EmotionsLog
        fields = ['id', 'user', 'emotion', 'description', 'count', 'date_joined']