from django.urls import path
from .views import LoginApiView, SignUpApiView, ActivateUserApiView

urlpatterns = [
    # path('logout/', account_views.LogoutView.as_view(), name='logout'),
    path('auth/login/', LoginApiView.as_view(), name='login'),
    path('auth/signup/', SignUpApiView.as_view()),
    path('auth/activate/<uidb64>/<token>/', ActivateUserApiView.as_view()),
]
