from rest_framework import serializers
from accounts.models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True ,
        required=True,
        style={'input_type': 'password'}
        )

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value
    
    def validate_email(slef, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists.')
        return value.lower()
    

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


