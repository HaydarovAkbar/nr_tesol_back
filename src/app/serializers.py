from rest_framework import serializers
from .models import Planners


class PlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planners
        fields = ('id', 'title', 'content', 'image')

    # def to_representation(self, instance):
    #     response = super(PlannerSerializer, self).to_representation(instance)
    #     response['created_at'] = instance.created_at.strftime('%Y-%m-%d %H:%M') if instance.created_at else None
    #     return response
