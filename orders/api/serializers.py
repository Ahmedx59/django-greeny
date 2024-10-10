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

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

        
class OrderDetailSerializer(serializers.ModelSerializer):
    products = OrderProductsSerializer(many=True , source = 'order')
    user = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = '__all__'

