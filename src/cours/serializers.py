from rest_framework import serializers
from .models import Teachers, CourseType, Courses


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ('id', 'fullname', 'position', 'avatar', 'about', 'is_boss', 'is_staff')


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
