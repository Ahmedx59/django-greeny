from rest_framework import viewsets , mixins
from rest_framework.decorators import action
from rest_framework.response import Response 


from .serializers import UserCreateSerializer , UserListSerializer ,UserRetrieveSerializer 
from accounts.models import User

class UserViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserListSerializer 

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        if self.action == 'retrieve':
            return UserRetrieveSerializer
        return super().get_serializer_class()
    


