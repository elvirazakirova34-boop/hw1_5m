from rest_framework import serializers
from apps.product.models import (Category, ProductModel, Product, ProductImage
)
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]

class ProductSerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "uuid", "title", "description", "price", "created_at", "is_active", "first_image"]  

    def get_first_image(self, obj):
        first_image = obj.product_images.first()
        if first_image:
            return ProductImageSerializer(first_image).data
        return None
    
class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category_title = serializers.CharField(source='category.title', read_only=True)
    model_title = serializers.CharField(source='model.title', read_only=True)

    class Meta:
        model = Product
        fields = ["id", "uuid", "title", "description", "price", "created_at", "is_active", "images", "category_title", "model_title"]

class ProductCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )

    class Meta:
        model = Product
        fields = ["category", "model", "title", "description", "price", "is_active", "images"]

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value
    
    def validate_price(self, value):
        if value <= '0':
            raise serializers.ValidationError("Price must be a positive number.")
        
    def validate(self, attrs):
        Category = attrs.get('category')
        ModelProduct = attrs.get('model')
        if Category and ModelProduct and ModelProduct.category != Category:
            raise serializers.ValidationError("Model does not belong to the specified category.")
        
        return super().validate(attrs)

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        
        request = self.context.get('request')
        product = Product.objects.create(user=request.user, **validated_data)

        for image in images_data:
            ProductImage.objects.create(product=product, image=image)
            
        return product
    
from rest_framework import serializers
from .models import Category, ProductModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

from rest_framework import viewsets
from .models import Category, ProductModel
from .serializer import CategorySerializer, ProductModelSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer