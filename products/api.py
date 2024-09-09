from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .models import productReview , ProductImages, Product , Brand , category
from .serializers import ProductsListSerializer , ProductsDetailSerializer



@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()
    data = ProductsListSerializer(products , many=True).data
    return Response(data)



@api_view(['GET'])
def product_detail_api(request,id):
    product = Product.objects.get(id=id)
    data = ProductsDetailSerializer(product).data
    return Response(data)



# @api_view(['DELETE'])
# def product_delete_api(request,id):
#     product = Product.objects.get(id=id)
#     product.delete()
#     return Response({'details':'delete successfully'})




class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer




class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsDetailSerializer
    
