from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from django.contrib.auth import get_user_model

CustomUser = get_user_model()

from ..base.serializers import Base64FileField
# User serilazers for token, register, update and login

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        # Get the user model
        User = get_user_model()

        # Check if the user exists
        try:
            user = User.objects.get(username=attrs['username'])
        except User.DoesNotExist:
            raise NotFound(detail="User not found", code=404)

        # Check if the user is active
        if not user.is_active:
            raise ValidationError("You are not allowed to login")

        # Call the parent validate method for further validation
        data = super().validate(attrs)
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        refresh_token = attrs.get('refresh')
        if not refresh_token:
            raise serializers.ValidationError("Refresh token is required.")
        return attrs

class UserMeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'middle_name',
            'password1',
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'gender',
            'date_of_birth',
            'address',
            'email',
            'region',
            'city',
            'is_student',
            'is_employee',
        )    


class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(validators=[validate_password],
                                    required=False, 
                                    allow_null=True, )
    
    image = Base64FileField(required=False, 
                             allow_null=True, 
                             default=None)

    username=serializers.CharField(required=False)
    phone_number=serializers.CharField(required=False)
    
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'image',
            'middle_name',
            'password',
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'gender',
            'date_of_birth',
            'address',
            'email',
            'region',
            'city',
            'is_student',
            'is_employee',
        )

    def create(self, validated_data):
        # Use validated_data to create a new user instance
        password = validated_data.pop('password')  # Extract password separately
        user = CustomUser.objects.create(**validated_data)
        user.password1=password
        user.set_password(password)  # Set hashed password
        user.save()
        return user

    def update(self, instance, validated_data):
        # Handle password updates securely
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)  # Update password if provided
        instance.save()
        return instance
    
    

class PasswordUpdateSerializer(serializers.ModelSerializer):
    employee_id = serializers.SerializerMethodField()  # Fixed field name

    class Meta:
        model = CustomUser
        fields = ["id", "employee_id", "password1"]
        read_only_fields = ["employee_id", "id"]

    def get_employee_id(self, obj):  # Fixed method name
        """Returns the employee ID for the user."""
        return getattr(obj, "employee", None) and obj.employee.id or None

    def validate_password(self, value):  # Fixed password validation
        """Validate the password field."""
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return value

    def update(self, instance, validated_data):
        """Handle password updates securely."""
        password1 = validated_data.pop("password1", None)

        if not password1:
            raise ValidationError({"password": "This field is required."})

        # Update the user's password securely
        instance.set_password(password1)
        instance.save()

        # Blacklist all outstanding tokens for the user
        self.blacklist_user_tokens(instance)

        return instance

    def blacklist_user_tokens(self, user):
        """Blacklist all outstanding JWT tokens for the user."""
        try:
            outstanding_tokens = OutstandingToken.objects.filter(user=user)
            for token in outstanding_tokens:
                BlacklistedToken.objects.get_or_create(token=token)
        except Exception as e:
            # Handle cases where tokens are not found (JWT not enabled)
            print(f"Token blacklisting error: {e}")