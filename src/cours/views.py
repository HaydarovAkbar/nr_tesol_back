from rest_framework import viewsets
from .models import Teachers, CourseType, Courses
from .serializers import (
    TeachersSerializer,
    CourseTypeSerializer, CoursesSerializer
)


class TeachersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Teachers.objects.filter(is_active=True)
    serializer_class = TeachersSerializer


class CourseTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CourseType.objects.filter(is_active=True)
    serializer_class = CourseTypeSerializer


class CoursesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Courses.objects.filter(is_active=True)
    serializer_class = CoursesSerializer
