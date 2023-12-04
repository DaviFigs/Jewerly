from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name="search"),
    path('search/<str:product_search>/', views.search, name="search_post"),    
    
]
