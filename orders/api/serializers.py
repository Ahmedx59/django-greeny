from rest_framework import serializers
from orders.models import Cart , CartDetail , Order , OrderDetail 
from products.api.serializers import ProductsListSerializer



class CartDetailSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = CartDetail
        fields = '__all__'



class CartSerializer(serializers.ModelSerializer):
    cart_derail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'



