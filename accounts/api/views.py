from rest_framework import viewsets, mixins

from accounts.models import User
from .serializers import UserSerializer, UserCreateSerializer

class UserViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    # def get_serializer_class(self):
    #     if self.action == 'post':
    #         print("="*100)
    #         return UserCreateSerializer
    #     return super().get_serializer_class()