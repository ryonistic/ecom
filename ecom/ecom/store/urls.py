from django.urls import path

from .views import (
CreateProduct,
add_to_cart
)

app_name = "store"
urlpatterns = [
        path('create_product/',CreateProduct.as_view(), name='create_product'),
        path('add_to_cart/<str:product_id>',add_to_cart, name='add_to_cart')
        ]
