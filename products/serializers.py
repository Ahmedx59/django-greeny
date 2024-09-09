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
        ]





class ProductsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'