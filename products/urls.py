from django.urls import path 
from .views import ProductList , ProductDetail , Brand_List ,Brand_Detail
from .api import  ProductListAPI , ProductDetailAPI , BrandListAPI , BrandDetailAPI , product_create_api , product_update_api , brand_create_api , brand_update_api




app_name = 'products'

# product/
urlpatterns = [
    path('',ProductList.as_view(), name='product_list' ),
    path('brand',Brand_List.as_view(), name= 'brand_list'  ),
    path('<slug:slug>',ProductDetail.as_view(), name= 'product_detail'),
    # path('brand/<int:pk>',Brand_Detail.as_view(), name='brand_detail'),



    # API
    path('api/list/', ProductListAPI.as_view()), 
    path('api/list/<int:pk>', ProductDetailAPI.as_view()),
    path('api/create/',product_create_api),
    path('api/brand_create/',brand_create_api),
    path('api/update/<int:pk>',product_update_api),
    path('api/brand_update/<int:pk>',brand_update_api),
    path('brand/api/list/',BrandListAPI.as_view()),
    path('brand/api/list/<int:pk>',BrandDetailAPI.as_view()),


]    
