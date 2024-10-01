from django.core.mail import send_mail
from rest_framework import serializers
from django.utils.crypto import get_random_string


from accounts.models import User 


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username')


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','image','phone_number','address','username','first_name','last_name','is_staff','is_active','date_joined')



    

class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True  , write_only=True)
    password = serializers.CharField(required=True  , write_only=True)
    class Meta:
        model = User
        fields = ('email','username','password','confirm_password')
        extra_kwargs = {
            'email':{'required':True}
        }

    def validate(self, attrs): 
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'detail':'the tow passwords does not match'}) 
        return super().validate(attrs)
    

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['is_active']=True
        validated_data['activation_code'] = get_random_string(20)
        user = User.objects.create_user(**validated_data)
        print(user,"="*100)
        send_mail(
            f"welcome{user.username}",
            f" her is code{user.activation_code}",
            "from@example.com",
            [user.email],
            fail_silently=False,
        )
         
        return user
         


    
