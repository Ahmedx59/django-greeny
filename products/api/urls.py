from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet , BrandViewSet , ReviewViewSet

router = DefaultRouter()
router.register('product-viewset' , ProductViewSet)
router.register('brands-viewset',BrandViewSet)
router.register(r'product-viewset/(?P<product_id>\d+)/review' ,ReviewViewSet)
urlpatterns = router.urls  