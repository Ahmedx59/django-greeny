from rest_framework import viewsets , mixins
from .serializers import UserCreateSerializer
from accounts.models import User

class UserViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer