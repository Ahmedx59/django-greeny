from django.shortcuts import render
from django.views import generic
from .models import Product
 





class ProductList(generic.ListView):
    model = Product

