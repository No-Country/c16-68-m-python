from rest_framework import serializers
from unapausa.models import CheckList, HealthyHabit


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = "__all__"
        # read_only_fields = ["user_id", "habit_id", "date_joined"]
        extra_kwargs = {"when_was_done": {"required": True, "allow_null": True}}


class HabitsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthyHabit
        fields = "__all__"