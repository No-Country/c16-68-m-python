from rest_framework import serializers
from unapausa.models import CheckList, HealthyHabit


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = "__all__"


class HabitsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthyHabit
        fields = "__all__"
