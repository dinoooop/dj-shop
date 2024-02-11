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
    path('api/users/profile/update/', views.updateUserProfile, name='update-user-profile'),
    path('api/users/', views.getUsers, name='users'),
    path('api/users/<str:pk>/', views.getUserById, name='update-user'),
    path('api/users/update/<str:pk>/', views.updateUser, name='update-user'),
    path('api/users/delete/<str:pk>/', views.deleteUser, name='delete-user'),
    path('api/orders/', views.getOrders, name='orders'),
    path('api/orders/add/', views.addOrderItems, name='add-order'),
    path('api/orders/myorders/', views.getMyOrders, name='myorders'),
    path('api/orders/<str:pk>/', views.getOrderById, name='user-order'),
    path('api/orders/<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
    path('api/orders/<str:pk>/deliver/', views.updateOrderToDelivered, name='deliver'),
    
]