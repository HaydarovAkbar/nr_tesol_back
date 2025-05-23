from django.urls import path
from .views import LoginApiView

urlpatterns = [
    # path('logout/', account_views.LogoutView.as_view(), name='logout'),
    path('login/', LoginApiView.as_view(), name='login'),
]
