from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import (
    Employee, 
    PassportOfEmployee, 
    EducationOfEmployee,
    Attachments,
)

from ..account.serializers import (
    UserSerializer
)
from ..base.serializers import Base64FileField
class EducationOfEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EducationOfEmployee
        fields='__all__'

class AttachmentCreateSerializer(serializers.ModelSerializer):
    # Adding file details to the serializer
    file_name = serializers.CharField(source='file.name', read_only=True)
    file_size = serializers.IntegerField(source='file.size', read_only=True)
    file = Base64FileField(required=False, allow_null=True)

    class Meta:
        model = Attachments
        fields = ['id', 'file', 'file_name', 'file_size', 'created_at', 'employee']

class AttachmentSerializer(serializers.ModelSerializer):
    # Adding file details to the serializer
    file_name = serializers.CharField(source='file.name', read_only=True)
    file_size = serializers.IntegerField(source='file.size', read_only=True)
    file = Base64FileField(required=False, allow_null=True)

    class Meta:
        model = Attachments
        fields = ['id', 'file', 'file_name', 'file_size', 'created_at']

class PassportOfEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PassportOfEmployee
        fields=[
            "country", 
            "document_number",
            "issue_date",
            "expiry_date",
            "is_id"
        ]


class EmployeeSerializer(WritableNestedModelSerializer):
    user=UserSerializer()
    passport=PassportOfEmployeeSerializer()
    attachments=AttachmentSerializer(required=False,many=True)
    class Meta:
        model=Employee
        fields=[
            "id",
            "user", 
            "work_position", 
            "status", 
            "passport", 
            "branch", 
            "marital_status",
            "attachments",
            "hire_date",
            "description"
        ]

    def validate(self, attrs):
        if attrs.get("work_position") == Employee.WorkPosition.DIRECTOR:
            branch = attrs.get("branch")
            if branch and Employee.objects.filter(
                branch=branch,
                work_position=Employee.WorkPosition.DIRECTOR
            ).exists():
                raise serializers.ValidationError(f"A director already exists for the branch {branch}.")
        return attrs    

class EmployeeListRetrieveSerializer(WritableNestedModelSerializer):
    user=UserSerializer(required=False,)
    passport=PassportOfEmployeeSerializer(required=False, )
    # attachments=AttachmentSerializer(required=False,many=True)
    branch = serializers.SerializerMethodField()
    class Meta:
        model=Employee
        fields=[
            "id",
            "user",
            "work_position", 
            "status", 
            "passport", 
            "branch", 
            "marital_status",
            "hire_date",
            "description"
        ]
    def get_branch(self, obj):
        """Returns branch UUID and name for GET requests."""
        if obj.branch:
            return {"id": obj.branch.id, "short_name": obj.branch.short_name, "legal_name":obj.branch.legal_name}
        return None


class EmployeePersonalInfoSerializer(WritableNestedModelSerializer):
    user=UserSerializer(required=False,) 

    class Meta:
        model=Employee
        fields=[
            "marital_status",
            "user"
        ]


class UpdateEmployeeDataserializer(WritableNestedModelSerializer):
    class Meta:
        model=Employee
        fields=['']
