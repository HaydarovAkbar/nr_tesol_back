from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Student, Passport, ParentOfStudent, Education, Attachments

from ..account.serializers import UserSerializer
class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = [
            "id",
            "country",
            "act_number",
            "document_number",
            "document_issue_date",
            "place_of_registration",
            "is_id",
        ]


class ParentOfStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentOfStudent
        fields = [
            "id",
            "last_name",
            "first_name",
            "middle_name",
            "date_of_birth",
            "phone_number",
            "email",
            "image",
            "note",
            "parental_status",
            "student",
        ]
        extra_kwargs = {
            "student": {"read_only": True},
        }


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            "id",
            "language",
            "additional_info",
            "level",
            "student",
        ]
        extra_kwargs = {
            "student": {"read_only": True},
        }


class AttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachments
        fields = [
            "id",
            "student",
            "file",
        ]
        extra_kwargs = {
            "student": {"read_only": True},
        }


class StudentSerializer(WritableNestedModelSerializer):
    passport = PassportSerializer(required=False, allow_null=True)
    parents = ParentOfStudentSerializer(many=True, required=False)
    education = EducationSerializer(many=True, required=False)
    attachments = AttachmentsSerializer(many=True, required=False)
    user=UserSerializer(required=False, allow_null=True)
    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "document_type",
            "passport",
            "parents",
            "education",
            "attachments",
        ]

    # def create(self, validated_data):
    #     passport_data = validated_data.pop("passport", None)
    #     parents_data = validated_data.pop("parents", [])
    #     education_data = validated_data.pop("education", [])
    #     attachments_data = validated_data.pop("attachments", [])
    #     user_data = validated_data.pop("attachments", [])
        
    #     student = super().create(validated_data)

    #     if passport_data:
    #         Passport.objects.create(student=student, **passport_data)
    #     for parent_data in parents_data:
    #         ParentOfStudent.objects.create(student=student, **parent_data)
    #     for education_item in education_data:
    #         Education.objects.create(student=student, **education_item)
    #     for attachment_data in attachments_data:
    #         Attachments.objects.create(student=student, **attachment_data)
        
    #     return student

    # def update(self, instance, validated_data):
    #     passport_data = validated_data.pop("passport", None)
    #     parents_data = validated_data.pop("parents", [])
    #     education_data = validated_data.pop("education", [])
    #     attachments_data = validated_data.pop("attachments", [])
        
    #     if passport_data:
    #         passport_instance, _ = Passport.objects.get_or_create(student=instance)
    #         for key, value in passport_data.items():
    #             setattr(passport_instance, key, value)
    #         passport_instance.save()
        
    #     for parent_data in parents_data:
    #         ParentOfStudent.objects.update_or_create(
    #             student=instance,
    #             **parent_data
    #         )
        
    #     for education_item in education_data:
    #         Education.objects.update_or_create(
    #             student=instance,
    #             **education_item
    #         )
        
    #     for attachment_data in attachments_data:
    #         Attachments.objects.update_or_create(
    #             student=instance,
    #             **attachment_data
    #         )
    #     return super().update(instance, validated_data)
