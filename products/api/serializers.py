from django.db.models.aggregates import Avg
from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,TaggitSerializer)
from ..models import ProductReview , Product , ProductImages , Brand , Category



class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductsListSerializer(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'id',
            'avg_rate',
            'name',
            'subtitle',
            'img',
            'flag',
            'price',
            'brand',
        ]

    def get_avg_rate(self, product):
        avg = product.product_review.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg']:
            return 0
        return avg['rate_avg']
    

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
    brand = serializers.PrimaryKeyRelatedField(queryset = Brand.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
    class Meta:
        model = Product
        fields ='__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    product = ProductsListSerializer(source = 'product_brand' , many=True)
    class Meta :
        model = Brand
        fields = '__all__'
