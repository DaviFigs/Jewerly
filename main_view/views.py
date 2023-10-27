from django.shortcuts import render
from products.models import Product

def home(request):
    product = Product.objects.all()
    context = {
        'product':product
    }

    return render(request, 'site.html', context)