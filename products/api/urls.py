from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet , BrandViewSet

router = DefaultRouter()
router.register('product-viewset' , ProductViewSet)
router.register('brands-viewset',BrandViewSet)

urlpatterns = router.urls