from django.shortcuts import render
from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework import filters as search_filter
from drf_spectacular.utils import OpenApiTypes, extend_schema
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status, generics

# Create your views here.
from  .filters import (
    AttachmentFilter,
    EmployeeFilter,
    
)

from ..base.paginations import TenPagination
from .models import (
    Employee,
    Attachments
)
from .serializer import(
    EmployeeSerializer,
    EmployeePersonalInfoSerializer,
    AttachmentSerializer,
    EmployeeListRetrieveSerializer,
    AttachmentCreateSerializer
)
class EmployeeCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = EmployeeSerializer
    queryset=Employee.objects.all()

class EmployeeListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = EmployeeListRetrieveSerializer
    queryset=Employee.objects.all()
    pagination_class=TenPagination
    filter_backends = (filters.DjangoFilterBackend,
                       search_filter.SearchFilter)
    
    search_fields = ['user__first_name','user__last_name', 'user__middle_name']
    filterset_class=EmployeeFilter

class EmployeeUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = EmployeeSerializer
    queryset=Employee.objects.all()
    lookup_field="id"

class EmployeePersonalInfoUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = EmployeePersonalInfoSerializer
    queryset=Employee.objects.all()
    lookup_field="id"

class EmployeePersonalInfoRetriveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = EmployeePersonalInfoSerializer
    queryset=Employee.objects.all()
    lookup_field="id"

class EmployeeDestroyView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = EmployeeSerializer
    queryset=Employee.objects.all()
    lookup_field="id"

class EmployeeRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = EmployeeListRetrieveSerializer
    queryset=Employee.objects.all()
    lookup_field="id"

class AttachmentsCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = AttachmentCreateSerializer
    queryset=Attachments.objects.all()

class AttachmentsListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = AttachmentSerializer
    queryset=Attachments.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       search_filter.SearchFilter)
    # search_fields = ['name',]
    filterset_class=AttachmentFilter

class AttachmentsUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = EmployeeSerializer
    queryset=Attachments.objects.all()
    lookup_field="id"

class AttachmentsDestroyView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = AttachmentSerializer
    queryset=Attachments.objects.all()
    lookup_field="id"

class AttachmentsRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = AttachmentSerializer
    queryset=Attachments.objects.all()
    lookup_field="id"