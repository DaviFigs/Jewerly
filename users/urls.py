from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('logout/', views.logout, name="logouts"),
    path('auth_login/', views.auth_login, name='auth_login'),
    path('auth_register/', views.auth_register, name="auth_register"),
    
]