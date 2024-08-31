from django.contrib import admin

from .models import Product ,productReview ,ProductImages ,category ,Brand


class ProductImgAdmin(admin.TabularInline):
    model = ProductImages


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImgAdmin, )


# admin.site.register(Product, ProductAdmin)
admin.site.register(productReview)
admin.site.register(ProductImages)
admin.site.register(category)
admin.site.register(Brand)
