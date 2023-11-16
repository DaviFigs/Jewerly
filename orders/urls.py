from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('finishing_purchase/', views.finishing_purchase, name="finishing_purchase")
]