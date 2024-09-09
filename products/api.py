from rest_framework import generics

from .models import productReview , ProductImages, Product , Brand , category
from .serializers import ProductsListSerializer , ProductsDetailSerializer , BrandListSerializer , BrandDetailSerializer






class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer




class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsDetailSerializer



class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer




class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer
    
