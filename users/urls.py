from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-view'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-edit'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),

    path('login/', TokenObtainPairView.as_view(permission_classes=[AllowAny]), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=[AllowAny]), name='token_refresh'),
]
