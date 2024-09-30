from rest_framework import serializers

from accounts.models import User 


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
        return User.objects.create_user(**validated_data)
         
    
