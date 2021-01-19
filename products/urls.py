from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('list/', views.products_list, name="products_list"),
    # path('list/<int:pk>/', views.create_product, name="product_create"),
    # path('list/<int:pk>/', views.update_product, name="product_update"),
    # path('list/<int:pk>/', views.delete_product, name="product_delete"),
]