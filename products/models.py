from django.db import models

class Discount(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=False)
    percent_by_price = models.DecimalField(max_digits=4, decimal_places=2,null=False)

class ProductCategory(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2,null=False)
    description = models.CharField(max_length=200, null=False)
    amount = models.IntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    num_sell = models.IntegerField(default=0)
