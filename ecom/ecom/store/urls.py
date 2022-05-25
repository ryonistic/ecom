from django.urls import path

from .views import (
CreateProduct,
ProductDetailView,
add_to_cart,
orders,
place_order,
CancelView, 
SuccessView, 
CreateCheckoutSessionView
)

app_name = "store"
urlpatterns = [
        path('create_product/', CreateProduct.as_view(), name='create_product'),
        path('place_order/', place_order, name='place_order'),
        path('orders/', orders, name='orders'),
        path('add_to_cart/<str:product_id>/', add_to_cart, name='add_to_cart'),
        path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
        path('cancel/', CancelView.as_view(), name='cancel'),
        path('success/', SuccessView.as_view(), name='success'),
        path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')

        ]
