from django import forms

from .models import Product, Review


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'type', 'description', 'image')

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content', 'stars')
