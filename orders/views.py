from django.shortcuts import render,redirect
from django.contrib.messages import constants
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required,login_required
from base import defs as df
import locale

#fazendo search
#objetos = Classe.objects.filter(name__contains = nome)
def finishing_purchase(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            products_ids = request.POST.getlist('check') #Here we just the products IDS, using the function below we get all products
            discount = request.POST.get('discount')

            products = df.get_products_by_ids(products_ids)
            purchase_discount = df.auth_discount(discount)

            total_price = df.get_total_price(products)
            
            context = {
                'products':products,
                'total_price':locale.currency(df.get_total_price_with_discount(purchase_discount, total_price))
            }
            messages.add_message(request, constants.INFO, 'Se algum cupom foi inserido, porém o preço não mudou, ele está incorreto!')
            return render (request, 'finishing_purchase.html',context)
        else:
            messages.add_message(request, constants.WARNING, 'Método HTTP inválido')
            return redirect('main')
    else:
        messages.add_message(request, constants.WARNING, 'Faça login para finalizar sua compra')
        return redirect('render_login')