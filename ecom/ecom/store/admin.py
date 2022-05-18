from django.contrib import admin

from .models import Cart, Order, Product

admin.site.register(Product)
admin.site.register(Cart)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('creator', 'date_placed')


