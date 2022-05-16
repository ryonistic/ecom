from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Product
from django.views.generic.list import ListView
from django.views.generic import CreateView
from .forms import ProductCreateForm

class HomeView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'pages/home.html'

class CreateProduct(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ProductCreateForm
    template_name = 'create_product.html'
    success_message = 'Product added!'
    success_url = reverse_lazy('home')
    
