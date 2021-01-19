from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50, help_text="상품 이름")
    image = models.ImageField(upload_to="product_main_image/%Y/%m/%d/", help_text="상품 대표 이미지") #image가 어디로 가는지는 조금 있다가!

    desc = models.TextField(blank=True, help_text="상품 설명")
    sell_price = models.IntegerField(default=0, help_text="현재 판매가")

    stock = models.IntegerField(help_text="상품 재고")
    sales_count = models.IntegerField(default=0, help_text="판매 수량")

    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey('users.User', related_name="products", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Product_Image(models.Model):
    image = models.ImageField(upload_to="product_images/%Y/%m/%d/", help_text="상품 이미지")

    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(Product, related_name="product_images", on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title