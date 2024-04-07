# market/forms.py
from django import forms
from .models import Product, BarterRequest

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'is_barter', 'image']

class BarterRequestForm(forms.ModelForm):
    class Meta:
        model = BarterRequest
        fields = ['message', 'phone_number', 'address']
