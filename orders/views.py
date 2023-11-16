from django.shortcuts import render


def finishing_purchase(request):
    return render (request, 'finishing_purchase.html')