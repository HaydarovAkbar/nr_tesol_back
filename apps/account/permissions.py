from rest_framework import permissions
from .models import CustomUser

class OnlyEmployeeCanPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        is_employee=CustomUser.objects.filter(id=request.user.id, is_employee=True, is_student=False).exists()
        return is_employee

class OnlyStudentCanPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        is_student=CustomUser.objects.filter(id=request.user.id, is_student=True, is_employee=False).exists()
        return is_student
    