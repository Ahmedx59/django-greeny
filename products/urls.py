from django.urls import path 
from .views import ProductList , ProductDetail , Brand_List

app_name = 'products'

# product/
urlpatterns = [
    path('',ProductList.as_view(), name='product_list' ),
    path('<slug:slug>',ProductDetail.as_view(), name= 'product_detail'),
    path('/brand',Brand_List.as_view(), name= 'brand_list'  ),

]