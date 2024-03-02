from rest_framework import serializers
from unapausa.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


class UserCreateSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)
    first_name = serializers.CharField(
        max_length=50, allow_blank=True, allow_null=True, required=False
    )
    last_name = serializers.CharField(
        max_length=50, allow_blank=True, allow_null=True, required=False
    )

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
            "firt_name",
            "last_name",
        ]

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()
        username_exists = User.objects.filter(username=attrs["username"]).exists()

        if email_exists:
            raise ValidationError("Email has already been used")
        elif username_exists:
            raise ValidationError("Username has already been used")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.username = validated_data.get("username", instance.username)
        instance.password = validated_data.get("password", instance.password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        extra_kwargs = {
            "first_name": {"required": False, "allow_blank": True, "allow_null": True},
            "last_name": {"required": False, "allow_blank": True, "allow_null": True},
        }


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=6)
    password = serializers.CharField(max_length=68, write_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "access_token", "refresh_token"]

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        request = self.context.get("request")
        user = authenticate(request, email=email, password=password)

        if not user:
            raise AuthenticationFailed("Invalid credentials, try again")
        # if not user.is_verified():
        # raise AuthenticationFailed('Email is not verified')
        user_tokens = user.tokens()

        return {
            "email": user.email,
            "access_token": str(user_tokens.get("access")),
            "refresh_token": str(user_tokens.get("refresh")),
        }


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    default_error_message = {"bad_token": " Token is Invalid or has expired"}

    def validate(self, attrs):
        self.token = attrs.get("refresh_token")
        return attrs

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except TokenError as error:
            return self.fail("bad_token")
