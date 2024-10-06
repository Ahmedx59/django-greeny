from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .serializers import CartSerializer
from orders.models import Cart , CartDetail 
from products.models import Product




class CartDetailCreateApi(generics.GenericAPIView):
    serializer_class = CartSerializer

    def get(self,request,*args,**kwargs):
        user = ''


    def post(self,request,*args,**kwargs):
        pass



    def delete(self,request,*args,**kwargs):
        pass