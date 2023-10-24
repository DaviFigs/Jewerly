from django.contrib import admin
from django.urls import path, include
from main_view import views

urlpatterns = [
    path('',views.home, name='main'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('base/', include ('base.urls')),
    path('main_view/', include('main_view.urls'))
]
