from django.urls import path

from .views import (
CreateProduct
)

app_name = "store"
urlpatterns = [
        path('create_product/',CreateProduct.as_view(), name='create_product')
        ]
