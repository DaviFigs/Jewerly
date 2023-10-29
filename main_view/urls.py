from django.urls import path
from . import views

urlpatterns = [
        path('user_historic/', views.render_hist, name="render_hist"),
        path('user_cart/', views.render_cart, name="render_cart"),

    
]
