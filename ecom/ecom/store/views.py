from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Cart, Product
from django.views.generic.list import ListView
from django.views.generic import CreateView
from .forms import ProductCreateForm
from django.contrib.auth.decorators import login_required

class HomeView(LoginRequiredMixin, ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_cart'] = get_object_or_404(Cart, owner=self.request.user)
        return context

@login_required
def cart_view(request):
    cart = get_object_or_404(Cart, owner=request.user)
    return render(request, 'pages/cart.html', {'cart':cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, owner=request.user)
    if product in cart.items.all():
        cart.items.remove(*[product])
        messages.success(request, 'Removed from cart')
    else:
        cart.items.add(*[product])
        messages.success(request, 'Added to cart')
    return redirect('cart')

class CreateProduct(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ProductCreateForm
    template_name = 'create_product.html'
    success_message = 'Product added!'
    success_url = reverse_lazy('home')
    
class ProductDetailView(LoginRequiredMixin, DetailView):

    model = Product
    template_name = 'pages/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_cart'] = get_object_or_404(Cart, owner=self.request.user)
        return context
