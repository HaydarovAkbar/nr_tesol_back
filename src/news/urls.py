from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NewsViewSet, FaqViewSet
)
from utils.views import (
    AboutViewSet, SettingsViewSet, PartnersViewSet, SolidFeatureViewSet, TestimonialsViewSet, DottedShapeViewSet
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
router.register(r'solid-feature', SolidFeatureViewSet)
router.register(r'testimonials', TestimonialsViewSet)
router.register(r'dotted-shape', DottedShapeViewSet)
router.register(r'faq', FaqViewSet)

urlpatterns = [
    path('platform/', include(router.urls)),
]
