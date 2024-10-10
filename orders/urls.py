from django.urls import path
from .views import OrderList 
from orders.api.views import CartDetailCreateApi , OrderListAPI , OrderDetailApi , CreateOrderAPI , ApplyCouponAPI



urlpatterns = [
    path('order',OrderList.as_view()),



    # api
    path('order/list/<str:username>' ,OrderListAPI.as_view()),
    path('order/list/<str:username>/create-order' ,CreateOrderAPI.as_view()),
    path('order/list/<str:username>/<int:pk>' ,OrderDetailApi.as_view()),
    path('order/<str:username>/cart',CartDetailCreateApi.as_view()),
    path('order/<str:username>/cart/apply-coupon',ApplyCouponAPI.as_view())
]
 