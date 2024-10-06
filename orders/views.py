from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required 
from .models import Order
from .models import Cart , CartDetail , Order , OrderDetail , Coupon
from products.models import Product


class OrderList(ListView):
    model = Order
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset().filter(user = self.request.user)
        return queryset
    

    def add_to_cart(request):
        quantity = request.POST['quantity']
        product = product.objects.get(id=request.POST['product_id'])

        cart = Cart.objects.get(user = request.user,status='InProgress')
        cart_detail , created = CartDetail.objects.get_or_create(cart=cart,product=product)
        cart_detail.quantity = int(quantity)  
        cart_detail.total = round(int(quantity)* product.price ,2)
        cart_detail.save()
        return{}


    def checkout(request):
        cart = Cart.objects.get(user = request.user,status='InProgress')
        cart_detail = CartDetail.objects.filter(cart=cart)
        return{}