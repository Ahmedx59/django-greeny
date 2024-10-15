from rest_framework import viewsets , mixins , status
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny

from .serializers import UserCreateSerializer , UserListSerializer ,UserRetrieveSerializer  , UserActivateSerializers , ChangePasswordSerializer , ForgetSerializer, ResetSerializer
from accounts.models import User

class UserViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet): 

    queryset = User.objects.all()
    serializer_class = UserListSerializer 
    # permission_classes = [AllowAny]
 
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        if self.action == 'retrieve':
            return UserRetrieveSerializer 
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action  in ['create','activate']:
            return [AllowAny()]
        return super().get_permissions()
    
    @action(detail=True , methods=['post'] , serializer_class=UserActivateSerializers)
    def activate(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception =True)
        serializer.save()
        return Response ({'detail':'your account successfully'},status=status.HTTP_200_OK)
    


class ChangePasswordViewSet(mixins.CreateModelMixin
                        ,viewsets.GenericViewSet):
    serializer_class = ChangePasswordSerializer
    permission_classes = [AllowAny]


    @action(detail=False , methods=['post'] , serializer_class=ForgetSerializer)
    def forget(self, *args, **kwargs):
        self.create(*args, **kwargs)
        return Response({'message':'email was sent'},status=status.HTTP_200_OK)
    
    @action(detail=True,methods=['post'])
    def reset(self, *args, **kwargs):
        token = self.kwargs['pk']
        data = self.request.data
        Serializer = ResetSerializer(data=data , context={'token':token})
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return Response({'detail':'password reset successfully'},status=status.HTTP_200_OK) 
