from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import PlannerSerializer, Planners


class PlannersViewSet(ReadOnlyModelViewSet):
    queryset = Planners.objects.filter(is_active=True)
    serializer_class = PlannerSerializer
