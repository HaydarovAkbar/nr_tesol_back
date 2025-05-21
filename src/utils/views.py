from rest_framework import viewsets
from .models import About, Settings, Partners
from .serializers import (
    AboutSerializer, SettingsSerializer,
    PartnersSerializer
)


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.filter(is_active=True)
    serializer_class = AboutSerializer


class SettingsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


class PartnersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partners.objects.filter(is_active=True)
    serializer_class = PartnersSerializer
