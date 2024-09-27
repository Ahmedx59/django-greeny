from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics , mixins , viewsets , filters 
from django_filters.rest_framework import DjangoFilterBackend


from ..models import ProductReview , ProductImages, Product , Brand , Category
from .serializers import ProductsListSerializer , ProductsDetailSerializer , BrandDetailSerializer , BrandListSerializer , ProductsCreateSerializer ,RivewListSerializer



class ProductViewSet(viewsets.ModelViewSet):
    queryset =Product.objects.all()
    serializer_class = ProductsListSerializer 
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['category', 'brand']
    search_fields = ['name', 'desc','subtitle']
    ordering_fields = ['price', 'quantity']
        

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductsDetailSerializer
        if self.action in ['create', 'update']:
            return ProductsCreateSerializer
        return super().get_serializer_class()


class ProductMerchantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BrandDetailSerializer
    
        return super().get_serializer_class()
    
class ReiviewCreateViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet): 
    
    queryset = ProductReview.objects.all()
    serializer_class = RivewListSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return super().get_queryset().filter(product=product_id)