from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from unapausa.models import CheckList, HealthyHabit
from rest_framework.exceptions import status
from .serializers import HabitsListSerializer, CheckListSerializer


# Create your views here.
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def get_habits(request):
    if request.method == "GET":
        queryset = HealthyHabit.objects.all()
        s = HabitsListSerializer(queryset, many=True)
        print(request.headers)
        print(s.data)
        return Response(s.data)
    return Response({"Bad http request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "POST", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def user_habits(request):
    if request.method == "GET":
        # s = HabitsListSerializer
        return Response({"You're log in"})
    if request.method == "POST":
        pass
