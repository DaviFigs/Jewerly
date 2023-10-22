from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    cpf = models.CharField(max_length=11, blank=True, null=True)
    past_buys = models.IntegerField(default=0)

