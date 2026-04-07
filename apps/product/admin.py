from django.contrib import admin

# Register your models here.
from apps.product.models import Category, ProductModel, Product, ProductImage

admin.site.register(Category)
admin.site.register(ProductModel)
admin.site.register(Product)
admin.site.register(ProductImage)