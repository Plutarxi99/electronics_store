from users import views
from users.apps import UsersConfig
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
app_name = UsersConfig.name

urlpatterns = [
    path('create/', views.UserCreateAPIView.as_view(), name='create-user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
