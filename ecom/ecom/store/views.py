from django.views.generic.base import TemplateView
from django.db.models import Q
import stripe
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Cart, Order, Product, Review
from django.views.generic.list import ListView
from django.views.generic import CreateView
from .forms import ProductCreateForm, ReviewCreateForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views import View

from .models import Price

stripe.api_key = settings.STRIPE_SECRET_KEY

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser

class CreateCheckoutSessionView(View):

    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.BASE_URL + '/store/success/',
            cancel_url=settings.BASE_URL + '/store/cancel/',
        )
        order = Order.objects.create(creator=request.user)
        order.save()
        order.items.add(*[price.product])

        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class HomeView(LoginRequiredMixin, ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_cart'] = get_object_or_404(Cart, owner=self.request.user)
        context['prices'] = Price.objects.all()
        return context

@login_required
def cart_view(request):
    cart = get_object_or_404(Cart, owner=request.user)
    total=0
    for item in cart.items.all():
        total += item.cost_price
    cart_total = total
    total_items = len(cart.items.all())
    return render(request, 'pages/cart.html', {'cart':cart, 'cart_total':cart_total, 'total_items':total_items})

@login_required
def orders(request):
    orders = Order.objects.filter(creator=request.user).order_by('-date_placed')
    return render(request, 'pages/orders.html', {'orders':orders})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, owner=request.user)
    if product in cart.items.all():
        cart.items.remove(*[product])
        messages.success(request, 'Removed from cart')
        return redirect('cart')
    else:
        cart.items.add(*[product])
        messages.success(request, 'Added to cart')
    return redirect('home')

@login_required
def place_order(request):
    cart = get_object_or_404(Cart, owner=request.user)
    total = 0
    if cart.items.all():
        for item in cart.items.all():
            total += item.cost_price
        if total > 1000:
            messages.info(request, 'Orders should be under 1000₹ in total.')
            return redirect('cart')
        else:
            order = Order.objects.create(creator=request.user)
            order.save()
            for item in cart.items.all():
                order.items.add(*[item])
            cart.items.clear()
            cart.save()
            messages.success(request, 'Order placed successfully.')
    else:
        messages.info(request, 'Cart is empty!')
    return redirect('cart')


class CreateProduct(SuperUserRequiredMixin, SuccessMessageMixin, CreateView):
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
        context['prices'] = Price.objects.filter(product__id=self.kwargs['pk'])
        context['reviews'] = Review.objects.filter(product__id=self.kwargs['pk'])
        context['form'] = ReviewCreateForm
        context['range1'] = range(1)
        context['range2'] = range(2)
        context['range3'] = range(3)
        context['range4'] = range(4)
        context['range5'] = range(5)
        return context

    def post(self, *args, **kwargs):
        form = ReviewCreateForm(self.request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.publisher = self.request.user
            review.product = Product.objects.get(id=self.kwargs['pk'])
            review.save()
            messages.success(self.request, 'Review was added.')
            return redirect('store:product_detail', self.kwargs['pk'])

# this search functionality makes use of icontains, which queries the DBMS for case-insensitive matches
def search(request, search_str):
	products = Product.objects.filter(Q(name__icontains=search_str) | Q(description__icontains=search_str))
	user_cart = get_object_or_404(Cart, owner=request.user)
	context = {'searched':search_str, 'products':products, 'user_cart':user_cart}
	return render(request, 'search_results.html', context)
