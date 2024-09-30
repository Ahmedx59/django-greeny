from django.urls import path
from rest_framework.routers import DefaultRouter

from accounts.api.views import UserViewSet

router = DefaultRouter()
router.register('users' , UserViewSet)

app_name = 'accounts'

urlpatterns = router.urls
