from django.core.mail import send_mail
from rest_framework.response import Response 
from rest_framework import serializers,status
from django.utils.crypto import get_random_string
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.contrib.auth.hashers import make_password , check_password

from accounts.models import User 


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username')


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','image','phone_number','address','username','first_name','last_name','is_staff','is_active','date_joined')




class UserCreateSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True , required = True)
    class Meta:
        model = User 
        fields = ('email','username','password','password_confirm')
        extra_kwargs = {
            'email':{'required':True},
            'password':{'required':True , 'validators':[MinLengthValidator(8)] , 'write_only':True}
        }
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({'detail':'not ok'})
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        validated_data['is_active'] = False
        validated_data['activation_code'] = get_random_string(20)
        user = User.objects.create_user(**validated_data)
        
        send_mail(
            f"Activation Code :",
            f"welcome {user.username}\n Here is the activation code : {user.activation_code}.",
            settings.EMAIL_HOST_USER,
            {user.email},
            fail_silently=False,
        )
        return user
    

class UserActivateSerializers(serializers.Serializer):
    code = serializers.CharField(required=True , write_only=True)

    def create(self, validated_data):
        user_id = self.context['view'].kwargs['pk']
        user = User.objects.get(id=user_id)
        if user.activation_code != validated_data['code']:
            raise serializers.ValidationError({'detail':'invalid Code'})
        user.is_active = True
        user.activation_code = ''
        user.save()
        return {}
 


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True , write_only=True)


    def validate(self, attrs):
        user= self.context['request'].user
        if not check_password(attrs['old_password'] , user.password):
            raise serializers.ValidationError({'error':'old password not equal password'})
        
       
        if attrs['new_password'] != attrs['confirm_new_password']:
            raise serializers.ValidationError({'error':'new password not equal confirm password'})
        
        return super().validate(attrs)
    

    def create(self, validated_data):
        user= self.context['request'].user
        user.set_password(validated_data['new_password'])
        user.save()
        
        return {}
        

    def to_representation(self, instance):
        return {'message': 'Password change process completed.'}

    
