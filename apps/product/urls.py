from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CategoryViewSet, ProductModelViewSet

from apps.product.views import (
    ProductViewSet
)

router = DefaultRouter()
router.register("product", ProductViewSet, basename='product')

urlpatterns = [
    
]

urlpatterns += router.urls

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductModelViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'models', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]