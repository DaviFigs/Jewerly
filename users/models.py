from django.db import models
from products.models import Product
from django.contrib.auth.models import AbstractUser

class Cart(models.Model):
    product = models.ManyToManyField(Product)
    def __str__(self):
        return self.pk
    
class Historic(models.Model):
    product = models.ManyToManyField(Product)
    def __str__(self):
        return self.pk

class MyUser(AbstractUser):
    profile_pic = models.ImageField(null= True, blank=True)
    cpf = models.CharField(max_length=11, blank=True, null=True, unique=True)
    past_buys = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart,blank=True, null=True, on_delete=models.CASCADE)
    historic = models.ForeignKey(Historic, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.username


