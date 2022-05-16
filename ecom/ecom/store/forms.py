from django import forms

from .models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'type', 'description', 'image')
