from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet , BrandViewSet, ProductMerchantViewSet, ReiviewCreateViewSet

router = DefaultRouter()
router.register('product-viewset' , ProductViewSet)
router.register(r'product-viewset/(?P<product_id>\d+)/reviews' , ReiviewCreateViewSet)
router.register('brands-viewset',BrandViewSet)
router.register('product-merchant',ProductMerchantViewSet)

urlpatterns = router.urls