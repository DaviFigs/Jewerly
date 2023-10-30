from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.render_login, name="render_login"),
    path('register/', views.render_register, name="render_register"),

    path('auth_login/', views.auth_login, name='auth_login'),
    path('auth_register/', views.auth_register, name="auth_register"),
    path('logout/', views.logout, name="logouts"),

    path('new_profile_pic/', views.new_profile_pic, name="new_profile_pic"),
    path('alter_data/', views.alter_data, name="alter_data"),
    
]