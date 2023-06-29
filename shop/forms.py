from django import forms
from .models import *

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'last_name', 'city', 'street', 'house', 'phone_number']

        widgets = {
        'name': forms.TextInput(attrs={"class":"form-control tall"}),
        'last_name': forms.TextInput(attrs={"class":"form-control tall"}),
        'city': forms.TextInput(attrs={"class":"form-control tall"}),
        'street': forms.TextInput(attrs={"class": "form-control tall"}),
        'house': forms.TextInput(attrs={"class": "form-control tall"}),
        'phone_number': forms.NumberInput(attrs={"class":"form-control tall"}),
        }


