from django.urls import path

from .views import (
CreateProduct,
ProductDetailView,
add_to_cart
)

app_name = "store"
urlpatterns = [
        path('create_product/',CreateProduct.as_view(), name='create_product'),
        path('add_to_cart/<str:product_id>/',add_to_cart, name='add_to_cart'),
        path('product_detail/<int:pk>/',ProductDetailView.as_view(), name='product_detail'),
        ]
