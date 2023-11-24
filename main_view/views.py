from django.shortcuts import render,redirect
from products.models import Product
from users.models import Cart, Historic
from django.contrib.messages import constants
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required,login_required
from base import defs as df
#from base.defs import prod_suggest,get_total_cart_price, get_all_products,filter_products,get_cart_products,get_hist_products\
#, get_product_by_id,get_products_by_ids


def home(request):
    if request.method != 'POST':
        context = {
            'products':df.get_all_products()
            }
        return render(request, 'site.html', context)
    else:
        try:
            filter =  request.POST.get('filter')
            context = {
                'products':df.filter_products(filter)
            }
            return render(request, 'site.html', context)
        except:
            messages.add_message(request, constants.WARNING, 'Selecione um filtro antes de clicar no botão!')
            return redirect('main')

@login_required(login_url = 'render_login')
def render_cart(request):
    try:
        products = df.get_cart_products(request)
        context = {
            'products':products,
            'total_price':df.get_total_price(products),
        }
        return render(request, 'cart.html',context)
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')


@login_required(login_url = 'render_login')
def render_profile(request):
    try:        
        context = {
            'hist_products':df.get_hist_products(request),
            'suggestion_products':df.prod_suggest(request),
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
                'products':df.get_all_products()
            }
            return render(request, 'product.html',context)
        else:
            messages.add_message(constants.WARNING, 'Este produto não existe')
            return redirect('main')
    except:
        messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente!')
        return redirect('main')


def render_buy(request, id):
    try:
        if request.method == 'GET':
            product_list = []
            product_list.append(df.get_product_by_id(id))

            context = {
                'buy_prod':df.get_product_by_id(id),
                'products':df.get_all_products(),
                'purchase_products':product_list,
                'cart_prod':df.get_cart_products(request),
            }
            return render(request, 'buy.html', context)

        if request.method == 'POST':
            products = request.POST.getlist('radio')
            product_list = df.get_products_by_ids(products)
            product_list.insert(0,df.get_product_by_id(id))
            context = {
                'buy_prod':df.get_product_by_id(id),
                'products':df.get_all_products(),
                'cart_prod':df.get_cart_products(request),
                'purchase_products':product_list,
                'total_price':df.get_total_price(product_list)
            }
            return render(request, 'buy.html', context)
    except:
        messages.add_message(request, constants.WARNING, 'Erro interno, tente novamente')
        return redirect(f'/your_buy/{id}/')
    
