from django.shortcuts import render
from django.db.models import Count
from rest_framework.response import Response
from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework import filters as search_filter
# Create your views here.

from .models import Branch
from .serializers import BranchSerializer
from .filters import BranchFilter

class BranchCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = BranchSerializer
    queryset=Branch.objects.all()

class BranchListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = BranchSerializer
    queryset=Branch.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       search_filter.SearchFilter)
    
    # search_fields = ['first_name','last_name', 'middle_name']
    filterset_class=BranchFilter

class BranchUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = BranchSerializer
    queryset=Branch.objects.all()
    lookup_field="id"

class BranchDestroyView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset=Branch.objects.all()
    serializer_class = BranchSerializer
    lookup_field="id"

class BranchRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = BranchSerializer
    queryset=Branch.objects.all()
    lookup_field="id"

    def get_queryset(self):
        return Branch.objects.annotate(
            employees_count=Count('employee'),
            students_count=Count('student'),
            classes_count=Count('classofbranch')
        )

    def get(self, request, *args, **kwargs):
        branch = self.get_object()
        serializer = self.get_serializer(branch)
        return Response(serializer.data)

    
