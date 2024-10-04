from django.urls import path
from .views import OrderList 



urlpatterns = [
    path('order',OrderList.as_view()),
    
]
