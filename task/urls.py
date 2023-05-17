from django.contrib import admin
from django.urls import path, include
from task import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('update/<str:pk>/', views.update, name = 'update'),
    path('delete/<str:pk>/', views.delete, name = 'delete')
]