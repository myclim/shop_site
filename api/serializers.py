from rest_framework import serializers
from shop.models import ProductModel, SubCategoryModel, CategoryModel





class CategoryApi(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'name']

class SubCategoryApi(serializers.ModelSerializer):
    category = CategoryApi(read_only=True)
    
    class Meta:
        model = SubCategoryModel
        fields = ['id', 'name', 'category']

class ProductApi(serializers.ModelSerializer):
    category = CategoryApi(read_only=True)
    
    class Meta:
        model = ProductModel
        fields = [
            'id',
            'name',
            'category',
            'short_description',
            'description',
            'price',
            'quantity',
            'discount',
        ]
        extra_kwargs = {
            'description': {'required': False},
            'quantity': {'min_value': 0},
        }
