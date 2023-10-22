from django.db import models
from products.models import Product, Discount
from users.models import MyUser

class Order(models.Model):
    user = models.ForeignKey(MyUser, null=False, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    discount = models.ForeignKey(Discount, null=True, blank=True,on_delete=models.CASCADE)
    total_value = models.DecimalField(max_digits=7, decimal_places=2,null=False) 
    final_value = models.DecimalField(max_digits=7, decimal_places=2, null=False) 
    finished = models.BooleanField(default=False)