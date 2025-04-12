from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .models import  (
    AcademicYear
)

from .serializers import (
    AcademicYearSerializer
)

class AcademicYearViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = AcademicYearSerializer
    queryset=AcademicYear.objects.all()

