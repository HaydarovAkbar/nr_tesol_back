from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NewsViewSet, AboutViewSet
)

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'about', AboutViewSet)

urlpatterns = [
    path('platform/', include(router.urls)),
]