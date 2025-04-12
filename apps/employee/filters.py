from django_filters import rest_framework as filters
from .models import Attachments, Employee



class AttachmentFilter(filters.FilterSet):
    employee_id=filters.CharFilter(field_name='employee__id', lookup_expr='exact')
    class Meta:
        model=Attachments
        fields=['employee_id', 'is_deleted']

class EmployeeFilter(filters.FilterSet):
    branch_id=filters.CharFilter(field_name='branch__id', lookup_expr='exact')
    work_position=filters.CharFilter(field_name='work_position', lookup_expr='exact')
    class Meta:
        model=Employee
        fields=['work_position','branch_id', 'is_deleted']
