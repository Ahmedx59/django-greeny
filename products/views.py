
from django.shortcuts import render
from django.views import generic
from .models import Product , ProductImages , ProductReview , Brand
 


# def queryset_debug(request):
#     # data = Product.objects.filter(price__gt=70)
#     data= Product.objects.filter(price__gte = 50)

#     return render(request,'product/debug.html',{'data':data})


class ProductList(generic.ListView):
    model = Product


class ProductDetail(generic.DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_image'] = ProductImages.objects.filter(product = self.get_object())
        context["reviews"] = ProductReview.objects.filter(product = self.get_object())
        context['related_product'] = Product.objects.filter(category = self.get_object().category)
        return context

    



class Brand_List(generic.ListView):
    model = Brand



class Brand_Detail(generic.DetailView):
    model = Brand 


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_brand"] = Product.objects.filter(brand = self.get_object()) 
        return context
    