from rest_framework import viewsets
from .models import News
from .serializers import (
    NewsSerializer
)


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = NewsSerializer
    lookup_field = 'uuid'