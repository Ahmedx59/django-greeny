from django.db.models.aggregates import Avg
from rest_framework import serializers

from .models import productReview , Product , ProductImages , Brand , category






class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = category
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
    
    brand = BrandListSerializer(read_only = True)
    category = CategoryListSerializer(read_only = True)

    class Meta:
        model = Product
        fields = '__all__'

class ProductsCreateSerializer(serializers.ModelSerializer):

    brand = serializers.PrimaryKeyRelatedField(queryset = Brand.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset = Brand.objects.all())

    class Meta:
        model = Product
        fields ='__all__'


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    product = ProductsListSerializer(source = 'product_brand' , many=True)
    class Meta :
        model = Brand
        fields = '__all__'


