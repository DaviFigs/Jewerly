from django.shortcuts import render,redirect
from products.models import Product
from users.models import Cart, Historic
from django.contrib.messages import constants
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required,login_required

def home(request):
    product = Product.objects.all()
    context = {
        'product':product}
    return render(request, 'site.html', context)

@login_required(login_url = 'render_login')
def render_cart(request):
    cart = Cart.objects.get(user = request.user)
    products = Product.objects.filter(cart = cart)
    context = {
        'cart':cart,
        'products':products
    }
    return render(request, 'cart.html',context)

@login_required(login_url = 'render_login')
def render_profile(request):
    historic = Historic.objects.get(user = request.user)
    hist_products = Product.objects.filter(historic = historic)
    context = {
        'hist_products':hist_products,
    }
    return render(request,'profile.html',context)

def render_jew(request, id):
    product = Product.objects.get(id = id)
    if product is not None:
        context = {
            'product':product,
        }
        return render(request, 'product.html',context)
    else:
        messages.add_message(constants.WARNING, 'Este produto não existe')
        return redirect('main')



    
