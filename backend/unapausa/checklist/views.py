from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from unapausa.models import CheckList, HealthyHabit
from rest_framework.exceptions import status
from .serializers import HabitsListSerializer, CheckListSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_habits(request):
    """
    This view return the habit list. At first make a query to get all habits, it pass through the serializer to convert this query set to json
    and return the data.
    """
    queryset = HealthyHabit.objects.all()
    s = HabitsListSerializer(queryset, many=True)
    return Response(s.data, status=status.HTTP_200_OK)


@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def user_habits(request, user_id):
    """
    This view recieve a url parameter, get that in mind.
    GET: get the list of the user, if there's no list for this user return a 404 code, otherwise
    return all the list from this users
    POST: Save the data into the db, if there already data from the same habit and the same data, i won't be saved and return an error.
    """
    if request.method == "GET":
        queryset = CheckList.objects.filter(user_id=user_id)
        if queryset:
            s = CheckListSerializer(queryset, many=True)
            return Response(s.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"The user hasn't create any lists yet"},
                status=status.HTTP_404_NOT_FOUND,
            )
    if request.method == "POST":
        print("IN POST")
        s = CheckListSerializer(
            data=request.data
        )  # Create a Serializer and pass the data
        if s.is_valid():  # To know if all the fields are correct
            isthereany = CheckList.objects.filter(
                user_id=user_id,
                habit_id=request.data["habit_id"],
                date_joined=request.data["date_joined"],
            )
            if isthereany:
                return Response(
                    {"This data already exists"}, status=status.HTTP_409_CONFLICT
                )
            s.save()  # Save to the db
            return Response(s.data, status=status.HTTP_200_OK)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PUT":
        # TODO: Check if this method work correctly
        # s = CheckListSerializer(data=request.data)
        if request.data.get("id"):
            try:
                queryset = CheckList.objects.get(
                    pk=request.data["id"],
                )
            except CheckList.DoesNotExist:
                return Response({"Data not found"}, status=status.HTTP)
            else:
                s2 = CheckListSerializer(queryset, data=request.data, partial=True)
                if s2.is_valid():
                    s2.save()
                    return Response(
                        {"The data was updated": s2.data}, status=status.HTTP_200_OK
                    )
                else:
                    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        # TODO: delete the data from the checklist
        s = CheckListSerializer(data=request.data)
        if s.is_valid() and request.data.get("id"):
            try:
                queryset = CheckList.objects.get(
                    pk=request.data["id"],
                )
            except CheckList.DoesNotExist:
                return Response({"Data not found"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                queryset.delete()
                return Response(
                    {"Data was deleted": CheckListSerializer(queryset).data},
                    status=status.HTTP_200_OK,
                )
