from django.urls import path
from .views import ProductList

# product/
urlpatterns = [
    path('',ProductList.as_view())

]
