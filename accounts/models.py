from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.utils.crypto import get_random_string



class User(AbstractUser):
    

    email = models.EmailField(_("email address"),unique=True, blank=True)
    image = models.ImageField(upload_to='user_image',blank=True, null=True)
    phone_number = models.CharField(max_length=50 , blank=True)
    address = models.CharField(max_length=100 , blank=True)
    facebook = models.URLField(max_length=200 , blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    activation_code = models.CharField(max_length=50, blank=True)
    reset_pass_token = models.CharField(max_length=50 , blank=True)
    reset_pass_expire_date = models.DateTimeField(null=True , blank=True) 
 

    # def save(self, *args, **kwargs):
    #    self.activation_code = get_random_string() 
       
    #    super().save(*args, **kwargs) # Call the real save() method



    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


    def __str__(self) -> str:
        return self.email





# class Profile(models.Model):
#     user = models.OneToOneField(User, related_name='Profile', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='profile_image',null=True ,blank=True)
#     phone_number = models.CharField(max_length=50,blank=True)
#     address = models.CharField(max_length=50,blank=True)

#     def __str__(self): 
#         return str(self.user)
    

    

# @receiver(post_save,sender=User)
# def profile_signal(sender , instance , created , **kwargs):
#     if created:
#         Profile.objects.create(
#             user = instance
#         )