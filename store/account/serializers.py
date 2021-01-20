from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'avatar']


# class RegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['email', 'full_name', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
#
#     def save(self):
#         account = User(
#             email=self.validated_data['email'],
#             full_name=self.validated_data['fullname'],
#
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#
#         if password != password2:
#             return serializers.ValidationError({'password': 'Password must be match'})
#         account.set_password(password)
#         account.save()
#         return account