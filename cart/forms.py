from django import forms
from .models import Cart

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['items_name', 'price', 'number_of_items', 'discount', 'quantity', 'description']