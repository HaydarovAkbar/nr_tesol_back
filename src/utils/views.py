from rest_framework import viewsets
from .models import About, Settings, Partners, SolidFeature, Testimonials, DottedShape
from .serializers import (
    AboutSerializer, SettingsSerializer,
    PartnersSerializer, SolidFeatureSerializer, TestimonialsSerializer, DottedShapeSerializer
)
from .pagination.base import SexPagination


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.filter(is_active=True)
    serializer_class = AboutSerializer


class SettingsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


class PartnersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partners.objects.filter(is_active=True)
    serializer_class = PartnersSerializer


class SolidFeatureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SolidFeature.objects.filter(is_active=True)
    serializer_class = SolidFeatureSerializer
    pagination_class = SexPagination


class TestimonialsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonials.objects.filter(is_active=True)
    serializer_class = TestimonialsSerializer


class DottedShapeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DottedShape.objects.filter(is_active=True)
    serializer_class = DottedShapeSerializer
