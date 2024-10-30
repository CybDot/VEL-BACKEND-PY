from rest_framework import serializers
from .models import VelNoteUser , UserFile
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid email or password')
        else:
            raise serializers.ValidationError('Email and password are required')

        attrs['user'] = user
        return attrs

class VelNoteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VelNoteUser
        fields = ['email', 'username', 'password', 'role']  # Include 'role' here
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = VelNoteUser(
            email=validated_data['email'],
            username=validated_data['username'],
            role=validated_data.get('role', 'receiver')  # Default role is 'receiver'
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VelNoteUser
        fields = ['role']
    
class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = ['file']




