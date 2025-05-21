from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NewsViewSet
)
from utils.views import (
    AboutViewSet, SettingsViewSet, PartnersViewSet
)
from cours.views import (
    TeachersViewSet, CourseTypeViewSet, CoursesViewSet
)

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'settings', SettingsViewSet)
router.register(r'partners', PartnersViewSet)
router.register(r'about', AboutViewSet)
router.register(r'teachers', TeachersViewSet)
router.register(r'courses', CoursesViewSet)
router.register(r'course-type', CourseTypeViewSet)

urlpatterns = [
    path('platform/', include(router.urls)),
]
