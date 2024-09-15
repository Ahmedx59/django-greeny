from django.urls import path


from .api import ProductGenericsAPIView , BrandGenericsAPIView


urlpatterns = [
    path('product/',ProductGenericsAPIView.as_view()),
    path('product/<int:pk>',ProductGenericsAPIView.as_view()),
    path('brand/',BrandGenericsAPIView.as_view()),
    path('brand/<int:pk>',BrandGenericsAPIView.as_view()),
]