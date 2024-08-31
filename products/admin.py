from django.contrib import admin

from .models import Product ,productReview ,ProductImages ,category ,Brand


admin.site.register(Product)
admin.site.register(productReview)
admin.site.register(ProductImages)
admin.site.register(category)
admin.site.register(Brand)
