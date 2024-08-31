from django.urls import path 
from .views import ProductList , ProductDetail

app_name = 'products'

# product/
urlpatterns = [
    path('',ProductList.as_view(), name='product_list' ),
    path('<int:pk>',ProductDetail.as_view(), name= 'product_detail'),
]