from django.shortcuts import render


def finishing_purchase(request):
    #getting the product buys
    products = request.POST.getlist('check')
    print(products)
    return render (request, 'finishing_purchase.html')

