from rest_framework import viewsets
from .models import News, About, Settings, Teachers, Partners, CourseType, Courses, Accreditation
from .serializers import (
    NewsSerializer, AboutSerializer, SettingsSerializer, TeachersSerializer,
    PartnersSerializer, CourseTypeSerializer, CoursesSerializer, AccreditationSerializer
)
from django_filters.rest_framework import DjangoFilterBackend
from utils.pagination.base import TenPagination


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = NewsSerializer
    lookup_field = 'uuid'
    pagination_class = TenPagination


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.filter(is_active=True)
    serializer_class = AboutSerializer


class SettingsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


class TeachersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Teachers.objects.filter(is_active=True)
    serializer_class = TeachersSerializer


class PartnersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partners.objects.filter(is_active=True)
    serializer_class = PartnersSerializer


class CourseTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CourseType.objects.filter(is_active=True)
    serializer_class = CourseTypeSerializer


class CoursesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Courses.objects.filter(is_active=True)
    serializer_class = CoursesSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['course_type', 'title']


class AccreditationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Accreditation.objects.filter(is_active=True)
    serializer_class = AccreditationSerializer
