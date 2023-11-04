from products.models import Product

def prod_suggest(hist_products:Product):
    total = 0
    if hist_products == 0:
        suggestions = Product.objects.filter(price__gte = 3)
        return suggestions
    else:
        for i in hist_products:
            total += i.price
        avg_user_products = total/len(hist_products)
        min_price = (avg_user_products*80)/100
        max_price = (avg_user_products*120)/100
        
        suggestions = Product.objects.filter( price__gte = min_price,price__lte = max_price)
        return suggestions