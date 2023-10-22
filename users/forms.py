from django.contrib.auth import forms
from . models import MyUser

class UserChangeForm(forms.UserChangeForm):#criamos um form para nosso user herdando do form padrão do django
    class Meta(forms.UserChangeForm.Meta):#na nossa classe meta herdamos a classe meta
        model = MyUser#definimos o nosso própio model

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = MyUser