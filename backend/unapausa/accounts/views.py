from django.shortcuts import render
from unapausa.models  import User
from .serializers import UserSerializer, UserCreateSerializer, LoginSerializer, LogoutSerializer, PasswordResetRequestSerializer, SetNewPasswordSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator


# Create your views here.

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    @swagger_auto_schema(
        operation_summary = "List all User",
        operation_descriptions = "Return a list of all users"
    )
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_summary = "Return an User by id",
        operation_descriptions = "Return an User details"
    )
    def get(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    @swagger_auto_schema(
        operation_summary = "Create an User"
    )
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "User Created Successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_summary = "Update an User"
    )
    def put(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "User Updated Successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserDeleteView(generics.DestroyAPIView):
    
    @swagger_auto_schema(
        operation_summary = "Delete an User"
    )
    def delete(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT) 


class LoginView(APIView):
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        operation_summary = "Login with jwt"
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestAuthenticationView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary = "Test token pair"
    )
    def get(self, request):
        data = {
            'msg': 'It works'
        }

        return Response(data=data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary = "Logout credentials"
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PasswordResetRequestView(generics.GenericAPIView):
    serializer_class=PasswordResetRequestSerializer

    @swagger_auto_schema(
        operation_summary = "Request for a password reset",
        operation_description = "It sends an email with a confirm link for verify the account email"
    )
    def post(self, request):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response({'message':'we have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        # return Response({'message':'user with that email does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    



class PasswordResetConfirm(generics.GenericAPIView):

    @swagger_auto_schema(
        operation_summary = "Password Reset Confirm",
        operation_description = "It takes uidb64 and token parameters for confirm"
    )
    def get(self, request, uidb64, token):
        try:
            user_id=smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'message':'token is invalid or has expired'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({'success':True, 'message':'credentials is valid', 'uidb64':uidb64, 'token':token}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:
            return Response({'message':'token is invalid or has expired'}, status=status.HTTP_401_UNAUTHORIZED)



class SetNewPasswordView(generics.GenericAPIView):
    serializer_class=SetNewPasswordSerializer

    @swagger_auto_schema(
        operation_summary = "Set a new password",
        operation_description = "It takes password, confirm password, uidb64 and token parameters for set a the new password"
    )
    def patch(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success':True, 'message':"password reset is succesful"}, status=status.HTTP_200_OK)