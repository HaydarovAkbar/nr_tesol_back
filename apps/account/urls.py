from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

urlpatterns=[
     path('login/', 
          views.MyObtainTokenPairView.as_view(), 
          name='token_obtain_pair'),
     path('login/refresh/', 
          TokenRefreshView.as_view(), 
          name='token_refresh'),
     path('logout/', 
          TokenBlacklistView.as_view(), 
          name='token_blacklist'),
     path('me/', 
          views.UserMeAPIView.as_view(), 
          name='user_me'),
     path('me/password/update/', 
          views.UserPasswordUpdateView.as_view(), 
          name='user_password_update'),
     path("employee/password/update/<uuid:employee_id>/", 
          view=views.EmployeePasswordUpdateAPIView.as_view(), 
          name="password_update")
]