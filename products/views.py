
from django.shortcuts import render
from django.views import generic
from .models import Product , ProductImages , productReview , Brand
 





class ProductList(generic.ListView):
    model = Product


class ProductDetail(generic.DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_image'] = ProductImages.objects.filter(product = self.get_object())
        context["reviews"] = productReview.objects.filter(product = self.get_object())
        context['related_product'] = Product.objects.filter(category = self.get_object().category)
        return context


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[""] = ''
        return context
    



class Brand_List(generic.ListView):
    model = Brand



class Brand_Detail(generic.DetailView):
    model = Brand 


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_brand"] = Product.objects.filter(brand = self.get_object()) 
        return context
    