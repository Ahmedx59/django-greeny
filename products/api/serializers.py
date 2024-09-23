from django.db.models.aggregates import Avg
from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,TaggitSerializer)
from ..models import ProductReview , Product , ProductImages , Brand , Category



class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductsListSerializer(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'subtitle',
            'img',
            'flag',
            'price',
            'brand',
        ]

    def get_avg_rate(self,product):
        avg = product.product_review.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg'] :
            result = 0 
            return result
        return avg['rete_avg']
    

class BrandListSerializer(serializers.ModelSerializer):
    class Meta :
        model = Brand
        fields = '__all__'


class ProductsDetailSerializer(serializers.ModelSerializer):
    
    brand = BrandListSerializer( )
    category = CategoryListSerializer(read_only = True)
    # tags = TagListSerializerField()

    class Meta:
        model = Product
        fields = '__all__'

class ProductsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'
    
    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user != instance.user:
            raise serializers.ValidationError({'detail':'you cant update this product'})
        return super().update(instance, validated_data)

class BrandDetailSerializer(serializers.ModelSerializer):
    product = ProductsListSerializer(source = 'product_brand' , many=True)
    class Meta :
        model = Brand
        fields = '__all__'



class Rev