from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product,productReview,ProductImages,Brand,category
from .serializers import ProductListSerializer


@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()
    data = ProductListSerializer(products, many=True).data
    return Response(data)