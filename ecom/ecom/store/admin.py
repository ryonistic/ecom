from django.contrib import admin

from .models import Cart, Order, Price, Product, Review

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Price)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('creator', 'date_placed')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('publisher', 'product', 'content', 'time_published', 'stars')
