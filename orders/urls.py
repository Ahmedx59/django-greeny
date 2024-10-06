from django.urls import path
from .views import OrderList 
from orders.api.views import CartDetailCreateApi



urlpatterns = [
    path('order',OrderList.as_view()),



    # api
    path('<srt:username>/cart',CartDetailCreateApi.as_view())
]
 