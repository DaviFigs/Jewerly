from django.shortcuts import render,redirect
from base import defs as df


#What is working right now
def search(request, product_name=''):
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
    
    elif request.method == 'POST':
        user_search = product_name
        search_filter = request.POST.get('filter')
        
        
        
