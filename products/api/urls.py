from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet , BrandViewSet, ProductMerchantViewSet

router = DefaultRouter()
router.register('product-viewset' , ProductViewSet)
router.register('brands-viewset',BrandViewSet)
router.register('product-merchant',ProductMerchantViewSet)

urlpatterns = router.urls