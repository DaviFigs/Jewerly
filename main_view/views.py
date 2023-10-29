from django.shortcuts import render,redirect
from products.models import Product
from users.models import Cart, Historic
from django.contrib.messages import constants
from django.contrib import messages
#This file just render all urls of website
#The rest of views proccess files and make the backend logic

def home(request):
    product = Product.objects.all()
    context = {
        'product':product}
    return render(request, 'site.html', context)

def render_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user = request.user)
        products = Product.objects.filter(cart = cart)
        context = {
            'cart':cart,
            'products':products
        }
        return render(request, 'cart.html',context)
    else:
        messages.add_message(request, constants.WARNING,'Para acessar o carrinho, registre-se ou faça login em sua conta!' )
        return redirect( 'render_login')
    
def render_hist(request):
    if request.user.is_authenticated:
        historic = Historic.objects.get(user = request.user)
        products = Product.objects.filter(historic = historic)
        context = {
            'historic':historic,
            'products':products
        }
        return render(request, 'historic.html', context)
    else:
        messages.add_message(request, constants.WARNING, 'Para acessar seu histórico, registre-se ou faça login em sua conta!')
        return redirect('render_login')



    
