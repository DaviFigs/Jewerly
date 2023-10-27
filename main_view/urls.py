from django.urls import path
from . import views

urlpatterns = [
        path('user_cart/', views.render_cart, name="render_cart"),
    
]
