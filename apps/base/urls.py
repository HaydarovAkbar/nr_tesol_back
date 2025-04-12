from django.urls import path
from . import views


urlpatterns = [
    path('static/countries/', views.CountryListAPIView.as_view(), name='country_list'),
    path('static/regions/', views.RegionListAPIView.as_view(), name='region_list'),
    path('static/districts/', views.DistrictsListAPIView.as_view(), name='district_list'),
]
