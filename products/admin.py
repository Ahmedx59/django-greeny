from django.contrib import admin

from .models import Product ,ProductReview ,ProductImages ,Category ,Brand

class ProductImageAdmin(admin.TabularInline):
    model = ProductImages

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
     inlines = (ProductImageAdmin,)

# admin.site.register(Product,ProductAdmin)
admin.site.register(ProductReview)
admin.site.register(ProductImages)
admin.site.register(Category)
admin.site.register(Brand)
