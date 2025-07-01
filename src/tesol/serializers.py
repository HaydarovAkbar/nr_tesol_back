from rest_framework import serializers
from .models import News, About, Settings, Teachers, Partners, CourseType, Courses, Accreditation, Services, Gallery, GalleryCategory


class NewsSerializer(serializers.ModelSerializer):
    # images = NewsImageSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ('uuid', 'title', 'content', 'image')

    def to_representation(self, instance):
        response = super(NewsSerializer, self).to_representation(instance)
        response['published_at'] = instance.published_at.strftime('%Y-%m-%d %H:%M') if instance.published_at else None
        return response


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'content', 'image')


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ('id', 'fullname', 'position', 'avatar', 'about', 'is_boss', 'is_staff')


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ('id', 'title', 'content', 'logo')


class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = ('id', 'title', 'attr', 'image')


class CoursesSerializer(serializers.ModelSerializer):
    teacher = TeachersSerializer(many=True, read_only=True)
    course_type = CourseTypeSerializer(read_only=True)

    class Meta:
        model = Courses
        fields = ('id', 'title', 'content', 'image', 'video', 'teacher', 'course_type')


class AccreditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accreditation
        fields = ('id', 'title', 'content', 'image')


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'title', 'content', 'image')


class GalleryCategorySerializer(serializers.ModelSerializer):
    """Gallery kategoriyalari uchun serializer"""

    class Meta:
        model = GalleryCategory
        fields = [
            'id',
            'title',
            'description',
            'slug',
            'is_active',
            'order'
        ]


class GalleryListSerializer(serializers.ModelSerializer):
    """Gallery ro'yxati uchun serializer"""
    category = GalleryCategorySerializer(read_only=True)
    media_url = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    tags_list = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = [
            'uuid',
            'title',
            'description',
            'media_type',
            'media_url',
            'thumbnail',
            'category',
            'alt_text',
            'tags_list',
            'is_featured',
            'view_count',
            'created_at',
            'published_at'
        ]

    def get_media_url(self, obj):
        return obj.get_media_url()

    def get_thumbnail(self, obj):
        return obj.get_thumbnail()

    def get_tags_list(self, obj):
        return obj.get_tags_list()


class GalleryDetailSerializer(serializers.ModelSerializer):
    """Gallery detali uchun serializer"""
    category = GalleryCategorySerializer(read_only=True)
    media_url = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    tags_list = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = [
            'uuid',
            'title',
            'description',
            'media_type',
            'media_url',
            'thumbnail',
            'image',
            'video_file',
            'video_url',
            'file_url',
            'external_url',
            'category',
            'alt_text',
            'tags_list',
            'is_featured',
            'view_count',
            'order',
            'created_at',
            'updated_at',
            'published_at'
        ]

    def get_media_url(self, obj):
        return obj.get_media_url()

    def get_thumbnail(self, obj):
        return obj.get_thumbnail()

    def get_tags_list(self, obj):
        return obj.get_tags_list()


class GalleryCreateUpdateSerializer(serializers.ModelSerializer):
    """Gallery yaratish va yangilash uchun serializer"""

    class Meta:
        model = Gallery
        fields = [
            'title',
            'description',
            'media_type',
            'image',
            'video_file',
            'video_url',
            'file_url',
            'external_url',
            'category',
            'alt_text',
            'tags',
            'is_featured',
            'order',
            'published_at'
        ]

    def validate(self, data):
        """Media turига қараб майдонларни текшириш"""
        media_type = data.get('media_type', 'image')

        if media_type == 'image' and not data.get('image'):
            raise serializers.ValidationError({
                'image': 'Rasm turi tanlanganda rasm fayli talab qilinadi.'
            })

        if media_type == 'video':
            if not data.get('video_file') and not data.get('video_url'):
                raise serializers.ValidationError({
                    'video': 'Video turi tanlanganda video fayli yoki URL talab qilinadi.'
                })

        if media_type == 'file' and not data.get('file_url'):
            raise serializers.ValidationError({
                'file_url': 'Fayl turi tanlanganda fayl talab qilinadi.'
            })

        return data