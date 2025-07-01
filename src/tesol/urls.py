from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NewsViewSet, AboutViewSet, SettingsViewSet,
    TeachersViewSet, PartnersViewSet, CourseTypeViewSet, CoursesViewSet, AccreditationViewSet, ServicesViewSet,
    GalleryCategoryListView, GalleryListView, GalleryDetailView, FeaturedGalleryView, PopularGalleryView,
    GalleryByMediaTypeView,
    search_gallery, gallery_stats
)

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='tesol-news')
router.register(r'about', AboutViewSet, basename='tesol-about')
router.register(r'settings', SettingsViewSet, basename='tesol-settings')
router.register(r'teachers', TeachersViewSet, basename='tesol-teachers')
router.register(r'partners', PartnersViewSet, basename='tesol-partners')
router.register(r'course-types', CourseTypeViewSet, basename='tesol-course-types')
router.register(r'courses', CoursesViewSet, basename='tesol-courses')
router.register(r'accreditation', AccreditationViewSet, basename='tesol-accreditation')
router.register(r'services', ServicesViewSet, basename='tesol-services')



urlpatterns = [
    path('tesol/', include(router.urls)),

    # Gallery URL larini alohida qo'shing:
    path('tesol/gallery/categories/', GalleryCategoryListView.as_view(), name='tesol-gallery-categories'),
    path('tesol/gallery/', GalleryListView.as_view(), name='tesol-gallery-list'),
    path('tesol/gallery/<uuid:uuid>/', GalleryDetailView.as_view(), name='tesol-gallery-detail'),
    path('tesol/gallery/featured/', FeaturedGalleryView.as_view(), name='tesol-gallery-featured'),
    path('tesol/gallery/popular/', PopularGalleryView.as_view(), name='tesol-gallery-popular'),
    path('tesol/gallery/type/<str:media_type>/', GalleryByMediaTypeView.as_view(), name='tesol-gallery-by-type'),
    path('tesol/gallery/search/', search_gallery, name='tesol-gallery-search'),
    path('tesol/gallery/stats/', gallery_stats, name='tesol-gallery-stats'),
]