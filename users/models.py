from django.db import models
from products.models import Product
from django.contrib.auth.models import AbstractUser

class Cart(models.Model):
    produto = models.ManyToManyField(Product)

class Historic(models.Model):
    produto = models.ManyToManyField(Product)

class MyUser(AbstractUser):
    cpf = models.CharField(max_length=11, blank=True, null=True, unique=True)
    past_buys = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart,blank=True, null=True, on_delete=models.CASCADE)
    historic = models.ForeignKey(Historic, blank=True, null=True, on_delete=models.CASCADE)



