from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import AccountsSerializer


class Signup(APIView):
    def post(self, request):
        serializer = AccountsSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(**request.data)
        response = AccountsSerializer(user)
        return Response(response.data, status=status.HTTP_201_CREATED)


class Login(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data['username'],
            password=request.data['password']
        )

        if user is None:
            return Response(status=status.HTTP_403_FORBIDDEN)

        token = Token.objects.get_or_create(user=user)[0]
        return Response({'token': token.key}, status=status.HTTP_200_OK)