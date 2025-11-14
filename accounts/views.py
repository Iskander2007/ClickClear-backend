from rest_framework import generics, permissions, response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from django.core import signing
from django.conf import settings
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def login_view(request):
    ser = LoginSerializer(data=request.data); ser.is_valid(raise_exception=True)
    user = ser.validated_data["user"]
    refresh = RefreshToken.for_user(user)
    return response.Response({
        "user": UserSerializer(user).data,
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    })

@api_view(["GET"])
def me(request):
    return response.Response(UserSerializer(request.user).data)

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def verify_email(request):
    token = request.data.get("token")
    data = signing.loads(token, salt="email-verify", max_age=60*60*24*3)
    user = User.objects.get(id=data["uid"])
    user.email_verified = True
    user.save()
    return response.Response({"ok": True})

@api_view(["POST"])
def logout_view(request):
    return response.Response({"ok": True})
