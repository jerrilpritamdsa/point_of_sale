from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['identity','name']
        
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','price','present_item']