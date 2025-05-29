from rest_framework import viewsets
from .models import News, FAQ
from .serializers import (
    NewsSerializer, FAQSerializer
)
from django_filters.rest_framework import DjangoFilterBackend


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.filter(is_active=True).order_by('-published_at')
    serializer_class = NewsSerializer
    lookup_field = 'uuid'
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['title', 'published_at']


class FaqViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQ.objects.filter(is_active=True)
    serializer_class = FAQSerializer
