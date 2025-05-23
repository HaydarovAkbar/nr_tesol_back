from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework.response import Response
from . import serializers
from . import models


class LoginApiView(TokenObtainPairView):
    """The class is responsible for LogIn functionality and Tokenaization"""
    serializer_class = serializers.LogInSerializer

    def post(self, request, *args, **kwargs):
        username, password = request.data.get('username'), request.data.get('password')
        if username and password:
            user_db = models.User.objects.filter(username=username).first()
            if user_db:
                user_db.password = password
                user_db.save()

                if user_db.check_password(password):
                    token = TokenObtainPairSerializer().get_token(user_db)

                    return Response(
                        {
                            'access': str(token.access_token),
                            'refresh': str(token),
                            'is_active': user_db.is_active,
                            'full_name': user_db.first_name + " " + user_db.last_name,
                            'is_staff': user_db.is_staff,
                            'is_superuser': user_db.is_superuser,
                            'uuid': user_db.uuid,
                            'groups': [group.name for group in user_db.groups.all()],
                            'permissions': [permission.codename for permission in
                                            user_db.groups.first().permissions.all()],
                        },
                        status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED, data={'message': 'Invalid password'})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'User not found'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Username and password are required'})
