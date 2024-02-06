from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('<str:pk>/', views.show, name='product'),
]