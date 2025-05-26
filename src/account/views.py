from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from . import serializers
from . import models
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class LoginApiView(TokenObtainPairView):
    """Login + Token returning with extra user info"""
    serializer_class = serializers.LogInSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'message': 'Username and password are required'}, status=400)

        user = authenticate(username=username, password=password)
        if user is not None:
            if not user.is_active:
                return Response({'message': 'User is inactive'}, status=403)

            refresh = RefreshToken.for_user(user)

            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'is_active': user.is_active,
                'full_name': f"{user.first_name} {user.last_name}",
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
                'organization': user.organization.title if user.organization else None,
                'uuid': str(user.uuid),
                'groups': [group.name for group in user.groups.all()],
                'permissions': [perm.codename for group in user.groups.all() for perm in group.permissions.all()]
            }, status=200)
        else:
            return Response({'message': 'Login or password is incorrect'}, status=401)


class LogoutApiView(APIView):
    """Foydalanuvchini logout qilish (refresh tokenni blacklistga yuboradi)"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response({"message": "Refresh token required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Foydalanuvchi chiqdi"}, status=status.HTTP_205_RESET_CONTENT)

        except TokenError:
            return Response({"message": "Noto‘g‘ri yoki eskirgan token"}, status=status.HTTP_400_BAD_REQUEST)



class SignUpApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = serializers.SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Ro‘yxatdan o‘tildi. Email orqali faollashtirish kerak."}, status=201)
        return Response(serializer.errors, status=400)


class ActivateUserApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = models.User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, models.User.DoesNotExist):
            return Response({"message": "Havola noto‘g‘ri yoki foydalanuvchi topilmadi"}, status=400)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({"message": "Hisob faollashtirildi. Endi login qilishingiz mumkin."}, status=200)
        else:
            return Response({"message": "Havola eskirgan yoki noto‘g‘ri"}, status=400)