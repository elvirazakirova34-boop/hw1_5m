from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.product.models import Product
from apps.product.serializer import (
    ProductCreateSerializer, ProductDetailSerializer,
    ProductSerializer
)

class ProductViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    
    def get_queryset(self):
        return (
            Product.objects.select_related("category", "model")
            .prefetch_related("product_image")
            .order_by("-created_at")
        )
    
    def get_serializer_class(self):
        if self.action == "create":
            return ProductCreateSerializer
        elif self.action == "retrieve":
            return ProductDetailSerializer
        return ProductSerializer

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        elif self.action == "retrieve":
            return [IsAuthenticated()]
        return [AllowAny()]
    
from rest_framework import viewsets
from .models import Category, ProductModel # Проверь названия моделей
from .serializer import CategorySerializer, ProductModelSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    
