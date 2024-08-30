from django.contrib import admin

from .models import Product ,productReview ,ProductImages ,category ,Brand



class ProductImageTabular(admin.TabularInline):
   model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageTabular]
    list_display = ['name','flag','quantitity','price']
    list_filter = ['flag','brand','category','price']
    search_fields = ['name','desc','subtitle']

admin.site.register(Product,ProductAdmin)
admin.site.register(productReview)
admin.site.register(ProductImages)
admin.site.register(category)
admin.site.register(Brand)
