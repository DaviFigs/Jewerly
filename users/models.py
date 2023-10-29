from django.db import models
from products.models import Product
from django.contrib.auth.models import AbstractUser
DEFAULT = "users_pics/default.jpg"

class MyUser(AbstractUser):
    profile_pic = models.FileField(null= True, blank=True, upload_to='users_pics', default=DEFAULT)
    cpf = models.CharField(max_length=11, blank=True, null=True, unique=True)
    past_buys = models.IntegerField(default=0)
    def __str__(self):
        return self.username

class Historic(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ManyToManyField(Product)
    def __str__(self):
        return f'Histórico de {self.user.first_name}'
    
class Cart(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ManyToManyField(Product)
    def __str__(self):
        return f'Carrinho de {self.user.first_name}'
