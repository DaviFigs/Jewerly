from django.shortcuts import render,redirect
from products.models import Product
from users.models import Cart
from django.contrib.messages import constants
from django.contrib import messages

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

def render_login(request):
    if request.user.is_authenticated:
        messages.add_message(request, constants.WARNING, 'Você já está logado!')
        return redirect('main')
    else:
        return render(request, 'login.html')
def render_register(request):
    if request.user.is_authenticated:
        messages.add_message(request, constants.WARNING, 'Você já está logado!')
        return redirect('main')
    else:
        return render(request,'signup.html')