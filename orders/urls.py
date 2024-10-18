from django.urls import path
from .views import OrderList 
from orders.api.views import CartDetailCreateApi ,OrderListAPI , OrderDetailApi , CreateOrderAPI



urlpatterns = [
    path('order',OrderList.as_view()),


    # api
    path('order/cart',CartDetailCreateApi.as_view()),
    # path('order/<str:username>/cart/apply-coupon',ApplyCouponAPI.as_view())
 
    path('order/list' ,OrderListAPI.as_view()),
    path('order/create-order' ,CreateOrderAPI.as_view()),
    path('order/<int:pk>' ,OrderDetailApi.as_view()),
]
 