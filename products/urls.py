from django.urls import path 
from .views import ProductList , ProductDetail , Brand_List ,Brand_Detail
from .api import product_list_api

app_name = 'products'

# product/
urlpatterns = [
    path('',ProductList.as_view(), name='product_list' ),
    path('brand',Brand_List.as_view(), name= 'brand_list'  ),
    path('<slug:slug>',ProductDetail.as_view(), name= 'product_detail'),
    path('brand/<int:pk>',Brand_Detail.as_view(), name='brand_detail'),


    # API
    path('api/list/', product_list_api),
]