from .models import Product
from django import forms

class FormProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "description",
            "amount",
            "amount",
            "category"]
