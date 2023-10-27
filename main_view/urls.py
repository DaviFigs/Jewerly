from django.urls import path
from . import views

urlpatterns = [
        path('user_cart/', views.render_cart, name="render_cart"),
        path('login/', views.render_login, name="render_login"),
        path('register/', views.render_register, name="render_register"),
    
]
