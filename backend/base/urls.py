from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/users/register/', views.registerUser, name='register'),
    path('api/users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/profile/', views.getUserProfile, name='user-profile'),
    path('api/users/', views.getUsers, name='users'),
    path('api/products/', views.getProducts, name='products'),
    path('api/products/<str:pk>/', views.getProduct, name='product'),
]