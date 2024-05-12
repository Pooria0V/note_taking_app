from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Account


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        # print('-'*20)
        # print(validated_data)
        # print(validated_data['username'])
        # print(validated_data['email'])
        # print(validated_data['password'])
        # print('-'*20)
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
