from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
    
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    image = models.ImageField( upload_to='profile-img', blank=True, null=True)
    phone_num = models.CharField( max_length=50, blank=True)
    address = models.CharField( max_length=50, blank=True)
    facebook = models.URLField( max_length=200, blank=True)
    twitter = models.URLField( max_length=200, blank=True)
    code = ''

    def __str__(self) -> str:
        return self.user

@receiver(post_save, sender=User)
def profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user= instance
        )