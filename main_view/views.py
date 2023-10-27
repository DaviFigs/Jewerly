from django.shortcuts import render
from products.models import Product
from users.models import Cart

def home(request):
    product = Product.objects.all()
    context = {
        'product':product
    }

    return render(request, 'site.html', context)

def render_cart(request):
    cart = Cart.objects.get()
    
    return render(request,'cart.html')