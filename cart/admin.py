from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'special_price']
    ordering = ['title']

admin.site.register(Product, ProductAdmin)
