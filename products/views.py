from django.shortcuts import render
from .models import Product, Product_Image
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def products_list(request):
    products = Product.objects.all()
    ctx = {
        'products':products,
    }
    return render(request, "products/list.html", ctx)
