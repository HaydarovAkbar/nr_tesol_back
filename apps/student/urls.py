from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet,
    PassportViewSet,
    ParentOfStudentViewSet,
    EducationViewSet,
    AttachmentsViewSet,
)

# Initialize DefaultRouter
router = DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"passports", PassportViewSet)
router.register(r"parents", ParentOfStudentViewSet)
router.register(r"education", EducationViewSet)
router.register(r"attachments", AttachmentsViewSet)

# Include the router in the URL patterns
urlpatterns = [
    path("", include(router.urls)),
]