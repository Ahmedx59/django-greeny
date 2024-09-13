from django.urls import path


from .api import ProductGenericsAPIView









urlpatterns = [
    path('product/',ProductGenericsAPIView.as_view()),
    path('product/<int:pk>',ProductGenericsAPIView.as_view()),
]