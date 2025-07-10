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
from app.views import (
    PlannersViewSet
)

router = DefaultRouter()
router.register(r'PlatformNews', NewsViewSet)
router.register(r'PlatformSettings', SettingsViewSet)
router.register(r'PlatformPartners', PartnersViewSet)
router.register(r'PlatformAbout', AboutViewSet)
router.register(r'PlatformTeacher', TeachersViewSet)
router.register(r'PlatformCourses', CoursesViewSet)
router.register(r'PlatformCourseType', CourseTypeViewSet)
router.register(r'PlatformSolidFeature', SolidFeatureViewSet)
router.register(r'PlatformTestimonials', TestimonialsViewSet)
router.register(r'PlatformDottedShape', DottedShapeViewSet)
router.register(r'PlatformFAQ', FaqViewSet)
router.register(r'PlatformPlanners', PlannersViewSet)

urlpatterns = [
    path('platform/', include(router.urls)),
]
