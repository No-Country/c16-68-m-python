from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from unapausa.models import CheckList, HealthyHabit
from rest_framework.exceptions import status
from .serializers import HabitsListSerializer, CheckListSerializer
from copy import deepcopy


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
# @permission_classes([IsAuthenticated])
def user_habits(request, user_id):
    """
    This view recieve a url parameter, get that in mind.
    GET: get the list of the user, if there's no list for this user return a 404 code, otherwise
    return all the list from this users
    POST: Save the data into the db, if there already data from the same habit and the same data, i won't be saved and return an error.
    PUT: it checks if the id of the checklist if in the data, make the query to find the data, and make a replacement for the when_was_done and is_done fields
    DELETE: Takes the id, search for it and if exits, delete the data and returns the deleted data
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
        data_copy = deepcopy(request.data)
        s = CheckListSerializer(data=data_copy)  # Create a Serializer and pass the data
        print(request.data)
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
            try:
                s.save()  # Save to the db
            except Exception as e:
                return Response({str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            else:
                return Response(s.data, status=status.HTTP_200_OK)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    # if request.method == "PUT":
    #     if request.data.get("id"):
    #         try:
    #             queryset = CheckList.objects.get(
    #                 pk=request.data["id"],
    #             )
    #         except CheckList.DoesNotExist:
    #             return Response({"Data not found"}, status=status.HTTP)
    #         else:
    #             s = CheckListSerializer(queryset, data=request.data, partial=True)
    #             if s.is_valid():
    #                 s.save()
    #                 return Response(
    #                     {"The data was updated": s.data}, status=status.HTTP_200_OK
    #                 )
    #             else:
    #                 return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return Response({"invalid Data"}, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "PUT":
        if request.data.get("id"):
            try:
                queryset = CheckList.objects.get(
                    pk=request.data["id"],
                )
            except CheckList.DoesNotExist:
                return Response({"Data not found"}, status=status.HTTP)
            else:
                s = CheckListSerializer(queryset, data=request.data, partial=True)
                if s.is_valid():
                    s.save()
                    return Response(
                        {"The data was updated": s.data}, status=status.HTTP_200_OK
                    )
                else:
                    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"invalid Data"}, status=status.HTTP_400_BAD_REQUEST)

        
        
        
    if request.method == "DELETE":
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
