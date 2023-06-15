from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'role', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data.get('email')
        username = validated_data.get('username')
        password = validated_data.get('password')
        role = validated_data.get('role', 'subscriber')
        try:
            user = User.objects.create_user(email=email, password=password, username=username, role=role)
        except ValidationError as e:
            raise serializers.ValidationError({'email': e})
        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            return data
        else:
            raise serializers.ValidationError('Email and password are required')