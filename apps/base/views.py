from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

# Create your views here.
from .countries import countries
from .regions import regions
from .districts import districts


class CountryListAPIView(APIView):
    
    @extend_schema(
        summary="Retrieve list of countries",
        description="This endpoint returns a list of all available countries.",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "countries": {
                        "type": "array",
                        "items": {"type": "string"},
                    }
                },
            }
        },
    )
    def get(self, request):
        return Response({"countries": countries})


class RegionListAPIView(APIView):
    @extend_schema(
        summary="Retrieve list of regions",
        description="This endpoint returns a list of all available regions.",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "regions": {
                        "type": "array",
                        "items": {"type": "string"},
                    }
                },
            }
        },
    )
    def get(self, request):
        return Response({"regions": regions})


class DistrictsListAPIView(APIView):
    @extend_schema(
        summary="Retrieve list of districts",
        description="This endpoint returns a list of all available districts.",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "districts": {
                        "type": "array",
                        "items": {"type": "string"},
                    }
                },
            }
        },
    )
    def get(self, request):
        return Response({"districts": districts})