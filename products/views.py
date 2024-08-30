from django.shortcuts import render
from django.views import generic

from .models import productReview,Product,ProductImages,Brand,category


class ProductList(generic.ListView):
    model = Product


