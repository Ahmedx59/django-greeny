from rest_framework import serializers
from orders.models import Cart , CartDetail , Order , OrderDetail 
from products.api.serializers import ProductsListSerializer
from products.models import Product




class CartDetailSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = CartDetail
        fields = '__all__'
 
 
class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = [
            'user',
            'status',
            'coupon',
            'total_after_coupon',
            'cart_detail'
        ]

class CartCreateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required = True)
    quantity = serializers.IntegerField(required = True)


    def create(self, validated_data):
        user = self.context['request'].user
        product = Product.objects.get(id=validated_data['product_id'])
        quantity = int(validated_data['quantity'])

        cart , created = Cart.objects.get_or_create(user=user, status='InProgress')
        cart_detail , created = CartDetail.objects.get_or_create(cart=cart, product=product)

        cart_detail.quantity = quantity 
        cart_detail.total = round(quantity* product.price ,2)
        cart_detail.save()

        return {}
    
    def to_representation(self, instance):
        return ({'message':'Product add successfully'})
    

# class DeleteCartDetailSerializer(serializers.ModelSerializer):
#     product_id = serializers.IntegerField(required = True)
#     quantity = serializers.IntegerField(required = True)



class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'





class OrderDetailSerializer(serializers.ModelSerializer):
    # products = OrderProductsSerializer(many=True , source = 'order')
    user = serializers.StringRelatedField() 
    class Meta:
        model = Order
        fields = '__all__'


# class OrderProductsSerializer(serializers.ModelSerializer):
#     # order_detail = OrderDetailSerializer(many=True)
#     class Meta:
#         model = Order
#         fields = (
#             'user',
#             'status',
#             'code',
#             'order_time',
#             'delivery_time',
#             'coupon',
#             'total_after_coupon',
#             # 'order_detail',
#         )


        
