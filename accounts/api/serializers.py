from rest_framework import serializers
from django.core.validators import MinLengthValidator

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ''


class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
            'confirm_password',
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
                "validators": [MinLengthValidator(8)],
                # "min_length": 8, 
                },
            "email":{"required":True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"Erorr":"The Two Passwords Doesn't Match"})
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user