from django.shortcuts import render
from base import defs as df
def search(request):
    typed = request.GET.get('search_by')
    product_list = df.search_products(typed)

    if len(product_list) == 0:
        product_list = 0
    context = {
        'search':typed,
        'products':product_list,
    }
    return render(request, 'search_list.html', context)
    
