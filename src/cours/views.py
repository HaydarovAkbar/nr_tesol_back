from rest_framework import viewsets
from .models import Teachers, CourseType, Courses
from .serializers import (
    TeachersSerializer,
    CourseTypeSerializer, CoursesSerializer
)
from django_filters.rest_framework import DjangoFilterBackend


class TeachersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Teachers.objects.filter(is_active=True)
    serializer_class = TeachersSerializer


class CourseTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CourseType.objects.filter(is_active=True)
    serializer_class = CourseTypeSerializer


class CoursesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Courses.objects.filter(is_active=True)
    serializer_class = CoursesSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['course_type', 'title']