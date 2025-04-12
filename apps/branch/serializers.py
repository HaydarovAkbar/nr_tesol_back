from .models import Branch
from django.contrib.gis.geos import Point
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from drf_writable_nested.serializers import WritableNestedModelSerializer

class BranchSerializer(WritableNestedModelSerializer):
    director = serializers.SerializerMethodField()
    employees_count = serializers.IntegerField(read_only=True)
    students_count = serializers.IntegerField(read_only=True)
    classes_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Branch
        # fields = [
        #     "id",
        #     "short_name",
        #     "legal_name",
        #     "stir",
        #     "phone_number",
        #     "web_site",
        #     "email",
        #     "region",
        #     "city",
        #     "address",
        #     "description",
        #     "longitude",
        #     "latitude",
        #     "status",
        #     "type_organization",
        #     "created_at",
        #     "director"
        # ]
        fields='__all__'

    def get_director(self, instance):
        from ..employee.models import Employee
        # Fetch the last director for the given branch
        director = Employee.objects.filter(
            work_position=Employee.WorkPosition.DIRECTOR,
            branch=instance
        ).last()
        if director:
            return {
            "id": director.id,
            "user_id": director.user.id if director.user else None,
            "full_name": director.user.full_name if director.user else None,
            "email": director.user.email if director.user else None,
            "marital_status": director.marital_status,
            "work_position": director.work_position,
            "status": director.status,
            "passport_id": director.passport.id if director.passport else None,
            "branch_id": director.branch.id if director.branch else None,
            "created_at": director.created_at,
            "updated_at": director.updated_at,
            }
        return None
