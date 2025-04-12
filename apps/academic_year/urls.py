from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Initialize DefaultRouter
router = DefaultRouter()
router.register(r"academic-year", views.AcademicYearViewSet)  # Ensure it's the correct viewset

urlpatterns = [
    path("", include(router.urls)),
]