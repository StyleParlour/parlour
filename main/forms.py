from django.forms import ModelForm
from django import forms
from .models import Product, Offers, Customers, Slot, Service


class SlotForm(ModelForm):
    class Meta:
        model = Slot
        fields = ['slotDate', 'slotTime']
        widgets = {
            'slotDate': forms.DateInput(attrs={'type': 'date'}),
            'slotTime': forms.TimeInput(attrs={'type': 'time'}),
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'brandName', 'currentStock', 'image']
        widgets = {
            'image': forms.FileInput(),
        }
