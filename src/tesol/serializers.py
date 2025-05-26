from rest_framework import serializers
from .models import News, About, Settings, Teachers, Partners, CourseType, Courses, Accreditation


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
