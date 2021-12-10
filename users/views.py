from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class Login(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password"))

        if not user:
            return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_403_FORBIDDEN)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)


class Logout(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        token = Token.objects.filter(user=request.user).first()
        token.delete()
        return Response(status=status.HTTP_200_OK)


class CreateUserView(CreateAPIView):
    model = User
    serializer_class = UserSerializer
