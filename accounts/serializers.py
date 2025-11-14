from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Roles
from django.core import signing
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "iin"]  # iin не возвращаем по API

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["email","password","role","phone","default_address","avatar_url"]
    def create(self, data):
        pwd = data.pop("password")
        user = User(**data)
        user.set_password(pwd)
        user.save()
        # письмо с подтверждением
        token = signing.dumps({"uid": user.id}, salt="email-verify")
        # В dev выводим ссылку в консоль:
        print("EMAIL VERIFY:", f"{settings.FRONTEND_BASE_URL}/verify-email?token={token}")
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self, attrs):
        user = authenticate(email=attrs["email"], password=attrs["password"])
        if not user: raise serializers.ValidationError("Неверный логин или пароль")
        return {"user": user}
