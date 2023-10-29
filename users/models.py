from django.db import models
from products.models import Product
from django.contrib.auth.models import AbstractUser
DEFAULT = "users_pics/default.jpg"

class Historic(models.Model):
    product = models.ManyToManyField(Product)
    def __str__(self):
        return str(self.pk)

class MyUser(AbstractUser):
    profile_pic = models.FileField(null= True, blank=True, upload_to='users_pics', default=DEFAULT)
    cpf = models.CharField(max_length=11, blank=True, null=True, unique=True)
    past_buys = models.IntegerField(default=0)
    historic = models.ForeignKey(Historic, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.username
    
class Cart(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ManyToManyField(Product)
    def __str__(self):
        return f'Carrinho de {self.user.first_name}'
