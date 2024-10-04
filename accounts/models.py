from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _
from django.utils.crypto import get_random_string
    
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class UserType(models.TextChoices):
        seller = 'seller'
        merchant = 'merchant'

    user_type = models.CharField(_("User Type"), max_length=50, choices=UserType.choices)
    email = models.EmailField(_("Email Address"), blank=True, unique=True)

    image = models.ImageField(_("Image"), upload_to='profile-img', blank=True, null=True)
    phone_num = models.CharField( max_length=50, blank=True, )
    address = models.CharField( max_length=50, blank=True)
    facebook = models.URLField( max_length=200, blank=True)
    twitter = models.URLField( max_length=200, blank=True)
    activation_code = models.CharField( max_length=50, blank=True)
    reset_pass_token = models.CharField( max_length=50, blank=True)
    reset_pass_expiration_date = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "user_type"]

    def __str__(self) -> str:
        return self.email

    # def save(self, *args, **kwargs):
    #     self.activation_code = get_random_string(20)
    #     super().save(*args, **kwargs)

# class Profile(models.Model):
#     user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    # image = models.ImageField( upload_to='profile-img', blank=True, null=True)
    # phone_num = models.CharField( max_length=50, blank=True)
    # address = models.CharField( max_length=50, blank=True)
    # facebook = models.URLField( max_length=200, blank=True)
    # twitter = models.URLField( max_length=200, blank=True)
    # code = ''

#     def __str__(self) -> str:
#         return f"{self.user} Profile"

# @receiver(post_save, sender=User)
# def profile_signal(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(
#             user= instance
#         )