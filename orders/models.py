from django.db import models
# from django.contrib.auth.models import User
from accounts.models import User

from django.utils import timezone
import datetime
from products.models import Product
from utils.generate_code import generate_code
 

class Cart(models.Model):
    class CartStatus(models.TextChoices):
        IN_PROGRESS = 'InProgress'
        COMPLETED = 'Completed'

    user = models.ForeignKey(User,related_name='user_cart',on_delete=models.SET_NULL , blank=True, null=True)
    status = models.CharField(max_length=10 , choices=CartStatus.choices , default=CartStatus.IN_PROGRESS)
    coupon = models.ForeignKey('Coupon', related_name='cart_coupon', on_delete=models.SET_NULL , blank=True, null=True)
    total_after_coupon = models.FloatField(blank=True, null=True)




    def __str__(self):
        return str(self.user)

    def  cart_total(self):
        total = 0
        for item in self.cart_detail.all():
            total += item.total 
        return round(total,2)


class CartDetail(models.Model):
    cart = models.ForeignKey(Cart,related_name='cart_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='cart_product',on_delete=models.SET_NULL , blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.cart)

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        RECEIVED ='Received'
        PROCESSED = 'Processed'
        SHIPPED = 'Shipped'
        DELIVERED = 'Delivered'

    user = models.ForeignKey(User,related_name='user_order',on_delete=models.SET_NULL , blank=True, null=True)
    status = models.CharField(max_length=10 , choices=OrderStatus.choices , default=OrderStatus.RECEIVED)
    code = models.CharField(max_length=20,default=generate_code)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(blank=True, null=True)
    coupon = models.ForeignKey('Coupon', related_name='order_coupon', on_delete=models.SET_NULL , blank=True, null=True)
    total_after_coupon = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.user)
    
    def save(self, *args, **kwargs):
       days = datetime.timedelta(days=5)
       self.delivery_time = self.order_time + days
       super().save(*args, **kwargs)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL , blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField()
    total = models.FloatField(blank=True, null=True)


    def __str__(self):
        return str(self.order)


class Coupon(models.Model):
    code = models.CharField(max_length=30)
    discount = models.IntegerField()
    quantity = models.IntegerField()
    order_time = models.DateTimeField(default=timezone.now)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.code
    

    def save(self, *args, **kwargs):
       week = datetime.timedelta(days=7)
       self.end_date = self.start_date + week 
       super(Coupon, self).save(*args, **kwargs) # Call the real save() method