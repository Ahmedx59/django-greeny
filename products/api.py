from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .models import productReview , ProductImages, Product , Brand , category
from .serializers import ProductsListSerializer , ProductsDetailSerializer , BrandDetailSerializer , BrandListSerializer





class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer




class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsDetailSerializer
    


class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer


class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer









@api_view(['POST'])
def product_create_api(request):
    data = request.data
    product = Product.objects.create(
        name = data.get('name'),
        subtitle = data.get('subtitle'),
        img = data.get('img'),
        sku = data.get('sku'),
        desc = data.get('desc'),
        flag = data.get('flag'),
        price = data.get('price'),
        quantitity = data.get('quantitity'),
        brand =  data.get('brand'),
    )    
    serializer = ProductsDetailSerializer(product).data
    return Response(serializer)


@api_view(['PATCH'])
def product_update_api(request,pk):
    product = Product.objects.get(id=pk)
    data = request.data

    product.name = data.get('name')
    product.subtitle = data.get('subtitle')
    product.img = data.get('img')
    product.sku = data.get('sku')
    product.desc = data.get('desc')
    product.flag = data.get('flag')
    product.price = data.get('price')
    product.quantitity = data.get('quantitity')

    brand = Brand.objects.get(id=data['brand'])
    product.brand = brand
    product.save()

    serializer = ProductsDetailSerializer(product).data
    return Response(serializer)









# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()
#     data = ProductsListSerializer(products , many=True).data
#     return Response(data)



# @api_view(['GET'])
# def product_detail_api(request,id):
#     product = Product.objects.get(id=id)
#     data = ProductsDetailSerializer(product).data
#     return Response(data)



# @api_view(['DELETE'])
# def product_delete_api(request,id):
#     product = Product.objects.get(id=id)
#     product.delete()
#     return Response({'details':'delete successfully'})
