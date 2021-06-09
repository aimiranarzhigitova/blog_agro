from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from agro_user.models import AgroUser
from agro_user.serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import *
from agro_user.permissions import *

class RegisterAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={
           'message': 'good',
           'status': 'CREATED'
        }, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'],
                            email=serializer.validated_data['email'],
                            password=serializer.validated_data['password'])
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'User not found or does not exist'})
        else:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'token': token.key},
                            status=status.HTTP_200_OK)

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (IsClient,)
        else:
            self.permission_classes = (AllowAny,)
        return [permission() for permission in self.permission_classes]