from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters

from .models import (
    Student, 
    Passport, 
    ParentOfStudent, 
    Education, 
    Attachments
)
from .serializers import (
    StudentSerializer,
    PassportSerializer,
    ParentOfStudentSerializer,
    EducationSerializer,
    AttachmentsSerializer,
)

from .filters import (
    StudentFilter,
    ParentOfStudentFilter,


)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = StudentFilter
    search_fields = ['user__first_name', 'user__last_name', 'user__middle_name']
    ordering_fields = ['user__first_name', 'user__last_name']\
    

    @action(detail=True, methods=["get"], url_path="parents")
    def get_parents(self, request, pk=None):
        student = self.get_object()
        parents = ParentOfStudent.objects.filter(student=student)
        serializer = ParentOfStudentSerializer(parents, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"], url_path="education")
    def get_education(self, request, pk=None):
        student = self.get_object()
        education = Education.objects.filter(student=student)
        serializer = EducationSerializer(education, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"], url_path="attachments")
    def get_attachments(self, request, pk=None):
        student = self.get_object()
        attachments = Attachments.objects.filter(student=student)
        serializer = AttachmentsSerializer(attachments, many=True)
        return Response(serializer.data)


class PassportViewSet(viewsets.ModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer




class ParentOfStudentViewSet(viewsets.ModelViewSet):
    queryset = ParentOfStudent.objects.all()
    serializer_class = ParentOfStudentSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ParentOfStudentFilter
    search_fields = ['first_name', 'last_name', 'middle_name']
    ordering_fields = ['first_name', 'last_name']

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class AttachmentsViewSet(viewsets.ModelViewSet):
    queryset = Attachments.objects.all()
    serializer_class = AttachmentsSerializer