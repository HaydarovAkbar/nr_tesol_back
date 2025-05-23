from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NewsViewSet, AboutViewSet, SettingsViewSet,
    TeachersViewSet, PartnersViewSet, CourseTypeViewSet, CoursesViewSet
)

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'about', AboutViewSet)
router.register(r'settings', SettingsViewSet)
router.register(r'teachers', TeachersViewSet)
router.register(r'partners', PartnersViewSet)
router.register(r'course-types', CourseTypeViewSet)
router.register(r'courses', CoursesViewSet)

urlpatterns = [
    path('tesol/', include(router.urls)),
]
