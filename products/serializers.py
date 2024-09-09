from rest_framework import serializers

from .models import productReview , Product , ProductImages , Brand , category

class ProductsListSerializer(serializers.ModelSerializer):
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


class ProductsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'




class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    product = ProductsListSerializer(source = 'product_brand' , many=True)
    class Meta :
        model = Brand
        fields = '__all__'