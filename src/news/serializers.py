from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('uuid', 'title', 'content', 'image')

    def to_representation(self, instance):
        response = super(NewsSerializer, self).to_representation(instance)
        response['published_at'] = instance.published_at.strftime('%Y-%m-%d %H:%M') if instance.published_at else None
        return response