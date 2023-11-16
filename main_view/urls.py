from django.urls import path
from . import views

urlpatterns = [
        path('user_cart/', views.render_cart, name="render_cart"),
        path('profile/', views.render_profile, name="render_profile"),  
        path('product/<int:id>/', views.render_jew, name="render_jew"),
        path('your_buy/<int:id>/', views.render_buy, name="render_buy"),
        
]
