from rest_framework import generics, serializers ,viewsets , mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from accounts.models import User
from .serializers import CartSerializer , OrderListSerializer  ,CartCreateSerializer , OrderDetailSerializer
from orders.models import Cart , CartDetail ,Order , OrderDetail , Coupon
from products.models import Product
import datetime 


class CartViewSet(
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,             
    viewsets.GenericViewSet
):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return super().get_queryset().filter(
            user=self.request.user, status = Cart.CartStatus.IN_PROGRESS
        )
    def get_serializer_class(self):
        if self.action == 'create':
            return CartCreateSerializer
        return super().get_serializer_class()
    
    
    
    
class OrderViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderDetailSerializer
        return super().get_serializer_class()
 










# class CartDetailCreateApi(generics.GenericAPIView):
#     serializer_class = CartSerializer

#     def get(self,request,*args,**kwargs):
#         user = request.user
#         cart , created = Cart.objects.get_or_create(user=user,status='InProgress')
#         data = CartSerializer(cart).data
#         return Response({'cart':data})
 
#     def post(self,request,*args,**kwargs):
#         user = request.user
#         product = Product.objects.get(id=request.data['product_id'])
#         quantity = int(request.data['quantity'])

#         cart , created = Cart.objects.get_or_create(user = user , status='InProgress')
#         cart_detail , created = CartDetail.objects.get_or_create(cart=cart, product=product)

#         cart_detail.quantity = quantity 
#         cart_detail.total = round(quantity* product.price ,2)
#         cart_detail.save()

#         data = CartSerializer(cart).data
#         return Response({'message':'Product add successfully', 'cart':data})
 
#     def delete(self,request,*args,**kwargs):
#         user = request.user
#         cart_detail = CartDetail.objects.get(id = request.data['cart_detail_id'])
#         cart_detail.delete()
#         cart = Cart.objects.get(user = user , status = 'InProgress')
#         data = CartSerializer(cart).data
#         return Response({'message':'product delete successfully', 'cart':data})
    

# class OrderListAPI(generics.ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderListSerializer
    
#     def list(self, request, *args, **kwargs):
#         user = request.user
#         queryset = self.get_queryset().filter(user=user)
#         data = OrderListSerializer(queryset , many=True).data
#         return Response(data )
     

    # def get(self):
    #     queryset = super(OrderListAPI , self).get_queryset()
    #     user = User.objects.get(username = self.kwargs['username'])
    #     queryset = queryset.filter(user=user)
    #     return queryset
    

# class OrderDetailApi(generics.RetrieveAPIView):
#     queryset = Order.objects.all()
#     serializer_class = ''


# class CreateOrderAPI(generics.GenericAPIView):

#     def post(self , request , *args, **kwargs):
#         user = request.user
#         cart, created = Cart.objects.get_or_create(user=user , status=Cart.CartStatus.IN_PROGRESS)
#         if created:
#             raise serializers.ValidationError({"message":"the cart is empty"})
        
#         cart_detail = CartDetail.objects.filter(cart=cart)

#         new_order = Order.objects.create(
#             user = user,
#             coupon = cart.coupon,
#             total_after_coupon = cart.total_after_coupon
#         )
        
#         for object in cart_detail:
#             OrderDetail.objects.create(
#                 order = new_order,
#                 product = object.product,
#                 quantity = object.quantity,
#                 price = int(object.product.price),  
#                 total = round(int(object.quantity)*object.product.price,2)
#             )
            
#         new_order.status = Order.OrderStatus.SHIPPED
#         cart.status = Cart.CartStatus.COMPLETED
#         new_order.save()
#         cart.save()

#         data = OrderProductsSerializer(new_order).data
#         return Response({'message':'Order created successfully','order':data})
  



# class ApplyCouponAPI(generics.GenericAPIView):
#     def post(self , request , *args, **kwargs):
#         user = request.user
#         cart = Cart.objects.get(user = user , status=Cart.CartStatus.IN_PROGRESS)
#         coupon = get_object_or_404(Coupon,code=request.data['coupon_code']) #->404
#         # coupon = Coupon.objects.get(code=request.data['coupon_code']) #->error

#         if coupon.quantity <= 0 or not coupon:
#             return Response({"message":"No coupon found"})
        
#         if cart.coupon == coupon:
#             raise serializers.ValidationError({"message":"you have applied this coupon before"})
        
#         today_date = datetime.datetime.today().date()
#         if not today_date >= coupon.start_date and not today_date <= coupon.end_date:
#             return Response({"message":"coupon date are not valid"})
        
#         coupon_value = cart.cart_total() * coupon.discount/100
#         cart_total = cart.cart_total() - coupon_value

#         coupon.quantity -= 1 
#         coupon.save()

#         cart.coupon = coupon
#         cart.total_after_coupon = cart_total
#         cart.save()
#         return Response({'message':'coupon applied successfully'})
        
        