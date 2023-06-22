# authentication/serializers.py

from django.contrib.auth import get_user_model
from rest_framework import serializers


from .models import Church, Community, Team

User = get_user_model()


from rest_auth.serializers import LoginSerializer

class CustomLoginSerializer(LoginSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)

        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class CustomLogoutSerializer(serializers.Serializer):
    pass



class ChurchSerializer(serializers.ModelSerializer):


    class Meta:
        model = Church
        fields = ['name', 'email']
       
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        if not self.context['request'].user.is_authenticated:
            raise serializers.ValidationError('User must be authenticated.')

        user = self.context['request'].user
        if not isinstance(user, User):
            raise serializers.ValidationError('User must be an instance of CustomUser.')

        validated_data['user'] = user
        church = Church.objects.create(**validated_data)
        return church


class PrayerResponseSerializer(serializers.Serializer):
    message = serializers.CharField()


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['name']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name']