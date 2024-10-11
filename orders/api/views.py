from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from accounts.models import User
from .serializers import CartSerializer , OrderListSerializer , OrderDetailSerializer , OrderProductsSerializer
from orders.models import Cart , CartDetail ,Order , OrderDetail , Coupon
from products.models import Product
import datetime 

class CartDetailCreateApi(generics.GenericAPIView):
    serializer_class = CartSerializer

    def get(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart , created = Cart.objects.get_or_create(user=user,status='InProgress')
        data = CartSerializer(cart).data
        return Response({'cart':data})

    def post(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        product = Product.objects.get(id=request.data['product_id'])
        quantity = int(request.data['quantity'])
        print(quantity,'='*100)

        cart = Cart.objects.get(user = user , status='InProgress')
        print(cart,'='*100)
        cart_detail , created = CartDetail.objects.get_or_create(cart=cart,product=product)
        cart_detail.quantity = quantity 
        cart_detail.total = round(quantity* product.price ,2)
        cart_detail.save()

        cart = Cart.objects.get(username = self.kwargs['username'])
        data = CartSerializer(cart).data
        return Response({'message':'Product add successfully', 'cart':data})
 
    def delete(self,request,*args,**kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart_detail = CartDetail.objects.get(id = request.data['cart_detail_id'])
        cart_detail.delete()
        cart = Cart.objects.get(user = user , status = 'InProgress')
        data = CartSerializer(cart).data
        return Response({'message':'product delete successfully', 'cart':data})
    

class OrderListAPI(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    


    def list(self, request, *args, **kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        queryset = self.get_queryset().filter(user=user)
        data = OrderListSerializer(queryset , many=True).data
        return Response(data )
     

    # def get(self):
    #     queryset = super(OrderListAPI , self).get_queryset()
    #     user = User.objects.get(username = self.kwargs['username'])
    #     queryset = queryset.filter(user=user)
    #     return queryset
    

class OrderDetailApi(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class CreateOrderAPI(generics.GenericAPIView):

    def get(self , request , *args, **kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart = Cart.objects.get(user = user , status='InProgress')
        cart_detail = CartDetail.objects.filter(cart=cart)
        new_order = Order.objects.create(
            user = user,
            coupon = cart.coupon,
            total_after_coupon = cart.total_after_coupon
        )
        for object in cart_detail:
            OrderDetail.objects.create(
                order = new_order,
                product = object.product,
                quantity = object.quantity,
                price = object.product.price,
                total = round(int(object.total)*object.product.price,2)
            )
        cart.status = 'Completed'
        cart.save()

        cart = Cart.objects.get(user = user , status = 'InProgress')
        data = CartSerializer(cart).data
        return Response({'message':'Order created successfully','cart':'data '})
  



class ApplyCouponAPI(generics.GenericAPIView):
    def post(self , request , *args, **kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart = Cart.objects.get(user = user , status='InProgress')
        coupon = get_object_or_404(Coupon,code=request.data['coupon_code']) #->404
        # coupon = Coupon.objects.get(code=request.data['coupon_code']) #->error
        if coupon and coupon.quantity > 0:
            today_date = datetime.datetime.today().date()

            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                coupon_value = cart.cart_total() * coupon.discount/100
                cart_total = cart.cart_total() - coupon_value

                coupon.quantity -= 1 
                coupon.save()

                cart.coupon = coupon
                cart.total_after_coupon = cart_total
                cart.save()
                return Response({'message':'coupon applied successfully'})
            else:
                return Response({"message":"coupon date are not valid"})
        
        else:
            return Response({"message":"No coupon found"})