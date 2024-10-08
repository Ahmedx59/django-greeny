from rest_framework import serializers
from django.core.validators import MinLengthValidator
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.conf import settings

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
        validated_data['is_active'] = False
        email = validated_data['email']
        validated_data['activation_code'] = get_random_string(20)

        user = User.objects.create_user(**validated_data)

        send_mail(
            "Your Activation Code",
            f'''welcome {user.username}.
            welocome to our store 
            Use this code {user.activation_code} to activate your account.''',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return user
    
class UserActivateSerializer(serializers.Serializer):
    code = serializers.CharField(required=True, write_only=True)

    def create(self, validated_data):
        code = validated_data['code']
        user = self.context['view'].get_object()
        if user.activation_code != code:
            raise serializers.ValidationError({"error":"The Code is not Vaild"})
        user.is_active = True
        user.activation_code = ""
        user.save()      
        return {}