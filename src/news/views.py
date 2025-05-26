from rest_framework import viewsets
from .models import News
from .serializers import (
    NewsSerializer
)
from django_filters.rest_framework import DjangoFilterBackend


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.filter(is_active=True).order_by('-published_at')
    serializer_class = NewsSerializer
    lookup_field = 'uuid'
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['title', 'published_at']
