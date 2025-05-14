from rest_framework import serializers
from . import models


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ('uuid', 'title', 'content', 'published_at')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['images'] = NewsImageSerializer(models.NewsImage.objects.filter(news=instance), many=True).data
        return ret


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsImage
        fields = ('id',)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['image'] = instance.get_image_url()
        return ret