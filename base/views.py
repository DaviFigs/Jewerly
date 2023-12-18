from django.shortcuts import render,redirect
from base import defs as df


def search(request):
    if request.method == 'GET':
        user_search = request.GET.get('search_by')
        product_list = df.search_products(user_search)

        if len(product_list) == 0:
            product_list = 0
        context = {
            'search':user_search,
            'products':product_list,
        }
        return render(request, 'search_list.html', context)
    
    elif request.method == 'POST':#adding filter on our code
        
        user_search = request.POST.get('user_search')
        search_filter = request.POST.get('search_filter')
        
        product_list = df.search_products(user_search)
        context= {
            'filter':search_filter,
            'search':user_search,
            'products':product_list,
        }
        return render(request, 'search_list.html', context)
        
        
