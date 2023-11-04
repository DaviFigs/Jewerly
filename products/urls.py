from django.urls import path, include
from . import views
urlpatterns = [
    path('prod_register/', views.prod_register, name="form_prod"),
    path('auth_prod_register/', views.auth_prod_register, name="auth_prod"),
]