from django.urls import path
from rest_framework.routers import DefaultRouter

from .api import ProductGenericsAPIView , BrandGenericsAPIView , ProductViewSet

router = DefaultRouter()
router.register('product-viewset' , ProductViewSet)

urlpatterns = [
    path('product/',ProductGenericsAPIView.as_view()),
    path('product/<int:pk>',ProductGenericsAPIView.as_view()),
    path('brand/',BrandGenericsAPIView.as_view()),
    path('brand/<int:pk>',BrandGenericsAPIView.as_view()),
]+router.urls