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
router.register(r'platform-news', NewsViewSet)
router.register(r'platform-settings', SettingsViewSet)
router.register(r'platform-partners', PartnersViewSet)
router.register(r'platform-about', AboutViewSet)
router.register(r'platform-teachers', TeachersViewSet)
router.register(r'platform-courses', CoursesViewSet)
router.register(r'platform-course-type', CourseTypeViewSet)
router.register(r'platform-solid-feature', SolidFeatureViewSet)
router.register(r'platform-testimonials', TestimonialsViewSet)
router.register(r'platform-dotted-shape', DottedShapeViewSet)
router.register(r'platform-faq', FaqViewSet)

urlpatterns = [
    path('platform/', include(router.urls)),
]
