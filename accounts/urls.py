from django.urls import path
from rest_framework.routers import DefaultRouter

from accounts.api.views import UserViewSet , ChangePasswordViewSet

router = DefaultRouter()
router.register('users' , UserViewSet)
router.register('password' , ChangePasswordViewSet , basename='change-password')

app_name = 'accounts'

urlpatterns = router.urls
