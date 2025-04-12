from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django_filters import rest_framework as filters
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from . import serializers
from . import models
# from .filters import StaffFilter


import logging

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.MyTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.LogoutSerializer

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserMeAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serialized_user = serializers.UserMeSerializer(user).data
        data = {
            'user': serialized_user,
            'notification_count':3
        }
        return Response(data, status=status.HTTP_200_OK)

class EmployeePasswordUpdateAPIView(generics.UpdateAPIView):
    serializer_class = serializers.PasswordUpdateSerializer
    queryset=models.CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field='employee_id'

    def get_object(self):
        """
        Ensure the lookup works correctly by fetching CustomUser based on the related Employee ID.
        """
        queryset = self.get_queryset()
        employee_id = self.kwargs.get(self.lookup_field)
        if not employee_id:
            raise NotFound("Employee ID is required for lookup.")
        return get_object_or_404(queryset, employee__id=employee_id)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class UserPasswordUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.PasswordUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user 