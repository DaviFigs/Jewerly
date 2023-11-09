from django.shortcuts import render,redirect
from products.models import Product
from users.models import Cart, Historic
from django.contrib.messages import constants
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required,login_required
from base.defs import prod_suggest,get_total_cart_price, get_all_products,filter_products,get_cart_products,get_hist_products


def home(request):
    if request.method != 'POST':
        context = {
            'products':get_all_products()
            }
        return render(request, 'site.html', context)
    else:
        try:
            filter =  request.POST.get('filter')
            context = {
                'products':filter_products(filter)
            }
            return render(request, 'site.html', context)
        except:
            messages.add_message(request, constants.WARNING, 'Selecione um filtro antes de clicar no botão!')
            return redirect('main')


@login_required(login_url = 'render_login')
def render_cart(request):
    try:
        products = get_cart_products(request)
        context = {
            'products':products,
            'total_price':get_total_cart_price(products),
        }
        return render(request, 'cart.html',context)
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')

@login_required(login_url = 'render_login')
def render_profile(request):
    try:        
        context = {
            'hist_products':get_hist_products(request),
            'suggestion_products':prod_suggest(request),
        }
        return render(request,'profile.html',context)
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')

def render_jew(request, id):
    try:
        product = Product.objects.get(id = id)
        if product is not None:
            context = {
                'product':product,
                'products':get_all_products()
            }
            return render(request, 'product.html',context)
        else:
            messages.add_message(constants.WARNING, 'Este produto não existe')
            return redirect('main')
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')

def render_buy(request, id):
    products = get_all_products()
    context = {
        'products':products
    }
    return render(request, 'buy.html', context)

    
