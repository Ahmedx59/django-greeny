from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from products.models import Product
from utils.generate_code import generate_code
 

CART_STATUS=(
    ('InProgress','InProgress'),
    ('Completed','Completed'),
)

ORDER_STATUS=(
    ('Received','Received'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)

class Cart(models.Model):
    user = models.ForeignKey(User,related_name='user_cart',on_delete=models.SET_NULL , blank=True, null=True)
    status = models.CharField(max_length=10 , choices=CART_STATUS)




class CartDetail(models.Model):
    cart = models.ForeignKey(Cart,related_name='cart_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='cart_product',on_delete=models.SET_NULL , blank=True, null=True)
    quantity = models.IntegerField()
    total = models.FloatField(blank=True, null=True)



class Order(models.Model):
    user = models.ForeignKey(User,related_name='user_order',on_delete=models.SET_NULL , blank=True, null=True)
    status = models.CharField(max_length=10 , choices=ORDER_STATUS)
    code = models.CharField(default=generate_code)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(blank=True, null=True)



class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL , blank=True, null=True)
    price = models.FloatField
    quantity = models.IntegerField()
    total = models.FloatField(blank=True, null=True)



class Coupon(models.Model):
    code = models.CharField(max_length=30)
    discount = models.IntegerField()
    quantity = models.IntegerField()
    oeder_time = models.DateTimeField(default=timezone.now)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.code
    

    def save(self, *args, **kwargs):
       week = datetime.timedelta(days=7)
       self.end_date = self.start_date + week 
       super(Coupon, self).save(*args, **kwargs) # Call the real save() method