from rest_framework import serializers
from orders.models import Cart , CartDetail , Order , OrderDetail 



class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = '__all__'



class CartSerializer(serializers.ModelSerializer):
    cart_derail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'



