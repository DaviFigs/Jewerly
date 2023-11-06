from products.models import Product
from users.models import Historic

def prod_suggest(request):
    total = 0
    historic = Historic.objects.get(user = request.user)
    hist_products = Product.objects.filter(historic = historic)
    if len(hist_products) ==0:
        hist_products = 0

    if hist_products == 0:
        return suggestions
    else:
        for i in hist_products:
            total += i.price
        avg_user_products = total/len(hist_products)
        min_price = (avg_user_products*50)/100
        max_price = (avg_user_products*150)/100
        
        suggestions = Product.objects.filter( price__gte = min_price,price__lte = max_price)
        return suggestions
    
def sum_price_prod(products) -> float:
    total = 0
    if products == 0:
        total = 0
        return total
    else:
        for i in products:
            total += i.price
        return total

def show_products():
    products = Product.objects.all()
    return products

def filter_products(filter):
    if filter == '1':
        min_price = 0;max_price = 300
    elif filter == '2':
        min_price = 301;max_price = 500
    elif filter == '3':
        min_price = 501;max_price = 800
    elif filter == '4':
        min_price = 801;max_price = 10000

    products = Product.objects.filter(price__gte = min_price, price__lte = max_price)
    return products
    
    
    