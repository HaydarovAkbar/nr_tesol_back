from rest_framework import serializers
from .models import About, Settings, Partners, SolidFeature, Testimonials, DottedShape


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'content', 'image')


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ('id', 'title', 'content', 'logo')


class SolidFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolidFeature
        fields = ('id', 'title', 'content')


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = ('id', 'title', 'content', 'image')


class DottedShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DottedShape
        fields = ('id', 'title', 'content', 'image')