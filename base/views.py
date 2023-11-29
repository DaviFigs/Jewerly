from django.shortcuts import render
from base import defs as df
def search(request):

    typed = request.GET.get('product_name')
    product_list = df.search_products(typed)
    print(product_list)
    context = {
        'search':typed,
        'products':product_list,
        'count':df.count_products(product_list)
    }
    return render(request, 'search_list.html', context)
    
