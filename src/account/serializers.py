from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers
from .models import User


class LogInSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs["is_active"] = self.user.is_active
        attrs["full_name"] = self.user.first_name + " " + self.user.last_name
        attrs["groups"] = [group.name for group in self.user.groups.all()]
        attrs["permissions"] = [permission.codename for permission in self.user.groups.first().permissions.all()]
        return attrs

    class Meta:
        model = User
        fields = ['username', 'password']


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name', 'phone_number', 'language')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Parollar mos emas")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.is_active = False  # Faollashtirish linkidan keyin faollashadi
        user.save()

        # Email orqali faollashtirish linkini yuborish
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        activation_link = f"{settings.FRONTEND_URL}/activate/{uid}/{token}"

        send_mail(
            subject="Foydalanuvchini faollashtirish",
            message=f"Salom {user.first_name},\n\nHisobingizni faollashtirish uchun quyidagi havolani bosing:\n{activation_link}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )

        return user
