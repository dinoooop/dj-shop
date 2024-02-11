from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='product-list'),
    path('create/', views.create, name='product-create'),
    path('upload/', views.uploadImage, name='product-upload-image'),
    path('update/<str:pk>/', views.update, name='product-update'),
    path('delete/<str:pk>/', views.delete, name='product-delete'),
    path('<str:pk>/reviews/', views.createProductReview, name="create-review"),
    path('<str:pk>/', views.detail, name='product-detail'),
]