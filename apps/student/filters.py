from django_filters import rest_framework as filters
from .models import (
    Attachments, 
    Student,
    ParentOfStudent
)

# class StudentFilter(filters.FilterSet):
#     student_id=filters.CharFilter(field_name='employee__id', lookup_expr='exact')
#     class Meta:
#         model=Attachments
#         fields=['employee_id']

class StudentFilter(filters.FilterSet):
    branch_id=filters.CharFilter(field_name='branch__id', lookup_expr='exact')
    grade_id=filters.CharFilter(field_name='grade__id', lookup_expr='exact')
    year_of_birth = filters.NumberFilter(field_name='user__date_of_birth', lookup_expr='year')

    class Meta:
        model=Student
        fields=['branch_id','grade_id', 'year_of_birth', 'is_deleted']
    
class ParentOfStudentFilter(filters.FilterSet):
    branch_id=filters.CharFilter(field_name='student__branch__id', lookup_expr='exact')
    grade_id=filters.CharFilter(field_name='student__grade__id', lookup_expr='exact')
    academic_year_id = filters.NumberFilter(field_name='student__grade__academic_year__id', lookup_expr='exact')
    class Meta:
        model=ParentOfStudent
        fields=['branch_id','grade_id', 'academic_year_id','is_deleted']