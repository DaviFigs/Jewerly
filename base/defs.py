from products.models import Product,Discount
from users.models import Historic,Cart
from django.db.models import Q


def search_products(typed):
    typed = typed.lower()
    products = Product.objects.filter(
        Q(name__icontains = typed)
        |Q(description__icontains = typed))
    return products

def get_product_by_id(id_prod):
    product = Product.objects.get(id = id_prod)
    if product is None:
        return 0
    else:
        return product
    
def get_products_by_ids(prod_list:list):
    prods_purchase = []
    prod_list = [int(id_prod) for id_prod in prod_list]
    for id_prod in prod_list:
        product = Product.objects.get(id = id_prod)
        if product is not None:
            prods_purchase.append(product)
    return prods_purchase
            
def prod_suggest(request):
    total = 0
    historic = Historic.objects.get(user = request.user)
    hist_products = Product.objects.filter(historic = historic)

    if len(hist_products) == 0:
        suggestions = get_all_products()
        return suggestions
    
    else:
        count =0
        for i in hist_products:
            total += i.price
            count +=1
        avg_user_products = total/count
        min_price = (avg_user_products*50)/100
        max_price = (avg_user_products*150)/100
        
        suggestions = Product.objects.filter( price__gte = min_price,price__lte = max_price)
        return suggestions
    
def get_cart_products(request):

    if request.user.is_authenticated:
        cart = Cart.objects.get(user = request.user)
        products = Product.objects.filter(cart = cart)
        if len(products) == 0:
            products = None;
            return products
        else:
            return products
    else:
        products = get_all_products()
        return products

def get_hist_products(request):
    historic = Historic.objects.get(user = request.user)
    hist_products = Product.objects.filter(historic = historic)
    if len(hist_products) == 0:
        hist_products = 0

    return hist_products

def auth_discount(code):
    code = code.lower()
    auth_code = Discount.objects.filter(name = code)

    if len(auth_code)>0:
        code = auth_code[0]
        discount =  code.percent_by_price
        return discount
        
    no_discount = Discount.objects.get(name = 'none')
    discount = no_discount.percent_by_price
    return discount

def get_total_price(products:list) -> float:
    total = 0
    if products is None:
        return total
    else:
        for i in products:
            total += i.price
        return total

def get_total_price_with_discount(discount, total_price):
    total_price = total_price - (total_price*discount/100)
    return total_price

def get_all_products():
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
    
def order_by_price():
    products = Product.objects.order_by('price')
    return products