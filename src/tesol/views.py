from rest_framework import viewsets
from .models import News, About, Settings, Teachers, Partners, CourseType, Courses, Accreditation, Services
from .serializers import (
    NewsSerializer, AboutSerializer, SettingsSerializer, TeachersSerializer,
    PartnersSerializer, CourseTypeSerializer, CoursesSerializer, AccreditationSerializer, ServicesSerializer,
    GalleryListSerializer,
    GalleryDetailSerializer,
    GalleryCategorySerializer,
    GalleryCreateUpdateSerializer
)

from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from django.utils import timezone
from .models import Gallery, GalleryCategory, GalleryView

from django_filters.rest_framework import DjangoFilterBackend
from utils.pagination.base import TenPagination


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = NewsSerializer
    lookup_field = 'uuid'
    pagination_class = TenPagination


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.filter(is_active=True)
    serializer_class = AboutSerializer


class SettingsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


class TeachersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Teachers.objects.filter(is_active=True).order_by('order')
    serializer_class = TeachersSerializer


class PartnersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partners.objects.filter(is_active=True)
    serializer_class = PartnersSerializer


class CourseTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CourseType.objects.filter(is_active=True)
    serializer_class = CourseTypeSerializer


class CoursesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Courses.objects.filter(is_active=True).order_by('order')
    serializer_class = CoursesSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['course_type', 'title']


class AccreditationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Accreditation.objects.filter(is_active=True)
    serializer_class = AccreditationSerializer


class ServicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Services.objects.filter(is_active=True)
    serializer_class = ServicesSerializer


class GalleryCategoryListView(generics.ListAPIView):
    """Gallery kategoriyalari ro'yxati"""
    queryset = GalleryCategory.objects.filter(is_active=True).order_by('order', 'title')
    serializer_class = GalleryCategorySerializer


class GalleryListView(generics.ListAPIView):
    """Gallery elementlari ro'yxati"""
    serializer_class = GalleryListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['media_type', 'category', 'is_featured']
    search_fields = ['title', 'description', 'tags', 'alt_text']
    ordering_fields = ['created_at', 'view_count', 'title', 'order']
    ordering = ['-created_at']
    pagination_class = TenPagination

    def get_queryset(self):
        queryset = Gallery.objects.filter(
            is_active=True,
            published_at__lte=timezone.now()
        ).select_related('category')

        # Kategoriya bo'yicha filtrlash
        category_slug = self.request.query_params.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        # Tag bo'yicha filtrlash
        tag = self.request.query_params.get('tag')
        if tag:
            queryset = queryset.filter(tags__icontains=tag)

        return queryset


class GalleryDetailView(generics.RetrieveAPIView):
    serializer_class = GalleryDetailSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        return Gallery.objects.filter(
            is_active=True,
            published_at__lte=timezone.now()
        ).select_related('category')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # Ko'rish statistikasini saqlash
        ip_address = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        gallery_view, created = GalleryView.objects.get_or_create(
            gallery=instance,
            ip_address=ip_address,
            defaults={'user_agent': user_agent}
        )

        if created:
            instance.increment_view_count()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_client_ip(self, request):
        """Mijoz IP manzilini olish"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class FeaturedGalleryView(generics.ListAPIView):
    """Tavsiya etilgan gallery elementlari"""
    serializer_class = GalleryListSerializer

    def get_queryset(self):
        return Gallery.objects.filter(
            is_active=True,
            is_featured=True,
            published_at__lte=timezone.now()
        ).select_related('category').order_by('order', '-created_at')[:10]


class PopularGalleryView(generics.ListAPIView):
    """Mashhur gallery elementlari"""
    serializer_class = GalleryListSerializer

    def get_queryset(self):
        return Gallery.objects.filter(
            is_active=True,
            published_at__lte=timezone.now()
        ).select_related('category').order_by('-view_count', '-created_at')[:10]


class GalleryByMediaTypeView(generics.ListAPIView):
    """Media turi bo'yicha gallery"""
    serializer_class = GalleryListSerializer

    def get_queryset(self):
        media_type = self.kwargs.get('media_type')
        return Gallery.objects.filter(
            is_active=True,
            media_type=media_type,
            published_at__lte=timezone.now()
        ).select_related('category').order_by('-created_at')


@api_view(['GET'])
def gallery_stats(request):
    """Gallery statistikasi"""
    total_items = Gallery.objects.filter(is_active=True).count()
    total_images = Gallery.objects.filter(is_active=True, media_type='image').count()
    total_videos = Gallery.objects.filter(is_active=True, media_type='video').count()
    total_files = Gallery.objects.filter(is_active=True, media_type='file').count()
    total_views = sum(Gallery.objects.filter(is_active=True).values_list('view_count', flat=True))

    return Response({
        'total_items': total_items,
        'total_images': total_images,
        'total_videos': total_videos,
        'total_files': total_files,
        'total_views': total_views,
        'categories_count': GalleryCategory.objects.filter(is_active=True).count()
    })


@api_view(['GET'])
def search_gallery(request):
    """Gallery qidirish"""
    query = request.GET.get('q', '')
    if not query:
        return Response({'results': []})

    results = Gallery.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(tags__icontains=query),
        is_active=True,
        published_at__lte=timezone.now()
    ).select_related('category')[:20]

    serializer = GalleryListSerializer(results, many=True)
    return Response({'results': serializer.data})
