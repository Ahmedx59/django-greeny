from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator , MaxValueValidator
from django.utils.text import slugify
from taggit.managers import TaggableManager


FLAG_OPTION = (
    ('New','New'),
    ('Feature','Feature'),
    ('Sale','Sale'),
    

)


class Product(models.Model):
    name = models.CharField(_("Name"),max_length=100)
    subtitle = models.CharField(_("Subtitle"),max_length=500,null=True,blank=True)
    img = models.ImageField(upload_to='Product_img' ,blank=True, null=True)
    sku = models.IntegerField(_("Sku"),null=True,blank=True)
    desc = models.TextField(_("Desccription"),max_length=10000,null=True,blank=True)
    flag = models.CharField(_("Flag"),max_length=10 , choices=FLAG_OPTION,null=True,blank=True)
    price = models.FloatField(_("Price"),null=True,blank=True)
    quantitity = models.IntegerField(_("Quantitity"),null=True,blank=True)
    brand = models.ForeignKey('Brand',related_name='product_brand',on_delete=models.SET_NULL, null=True,blank=True)
    category = models.ForeignKey('Category',related_name='product_category',on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    slug = models.SlugField(_("") ,null=True , blank= True)



    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super().save(*args, **kwargs)


class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')


    def __str__(self):
        return str(self.product)



class Brand(models.Model):
    name = models.CharField(_("Name"),max_length=100)
    image = models.ImageField(_("Image"),upload_to='brands/')

    def __str__(self):
        return self.name



class category(models.Model):
    name = models.CharField(_("Name"),max_length=100)
    image = models.ImageField(_("Image"),upload_to='categories/')

    def __str__(self):
        return self.name



class productReview(models.Model):
    user = models.ForeignKey(User,related_name='user_review',verbose_name=_("User"),on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='product_review',verbose_name=_("Product"),on_delete=models.CASCADE)
    rate = models.IntegerField(_("Rate"),validators=[MaxValueValidator(5),MinValueValidator(0)]) 
    review = models.TextField(_("Review"),max_length=1000)
    created_at = models.DateTimeField(_("Created at"),default=timezone.now)


    def __str__(self):
        return str(self.user)