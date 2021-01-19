from django.contrib import admin
from .models import Product, Product_Image

# Register your models here.

@admin.register(Product)
class CustomProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'sell_price'
    )

@admin.register(Product_Image)
class CustomProductAdmin(admin.ModelAdmin):
    pass