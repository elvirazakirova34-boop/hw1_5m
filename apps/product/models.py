from django.db import models
from apps.user.models import User
import uuid

class Category(models.Model):
    title = models.CharField(max_length=155, verbose_name="Название категории")
    image = models.ImageField(upload_to='category', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

class ProductModel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255, verbose_name="Название модели")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_product"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name="category_product",
        blank=True, null=True
    )
    model = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE,
        related_name="model_product",
        blank=True, null=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    title = models.CharField(
        max_length=255
    )
    description = models.TextField()
    price = models.CharField(
        max_length=15
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title
    
class ProductImage(models.Model):
    image = models.ImageField(
        upload_to='product'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='product_image'
    )