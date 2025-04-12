from django_filters import rest_framework as filters
from .models import Branch



class BranchFilter(filters.FilterSet):

    class Meta:
        model=Branch
        fields=['is_deleted']


