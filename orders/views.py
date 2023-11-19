from django.shortcuts import render,redirect
from django.contrib.messages import constants
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required,login_required
from base import defs as df



def finishing_purchase(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            products_ids = request.POST.getlist('check') #Here we just the products IDS, using the function below we get all products
            discount = request.POST.get('discount')
            purchase_discount = df.auth_discount(discount)
            print(purchase_discount)
            products = df.get_products_by_ids(products_ids)
            context = {
                'products':products,
                'total_price':df.get_total_price_with_discount(purchase_discount, df.get_total_price(products))
            }
            return render (request, 'finishing_purchase.html',context)
        else:
            messages.add_message(request, constants.WARNING, 'Método HTTP inválido')
            return redirect('main')
    else:
        messages.add_message(request, constants.WARNING, 'Faça login para finalizar sua compra')
        return redirect('render_login')