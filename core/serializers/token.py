from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'email': attrs.get('email'),
            'password': attrs.get('password')
        }

        user_email = authenticate(**credentials)
        credentials['email'] = None
        credentials['username'] = attrs.get('username')

        user_username = authenticate(**credentials)

        if user_email and user_username and user_email != user_username:
            msg = 'Only one of email/username must be provided.'
            raise serializers.ValidationError(msg, code='authorization')

        user = user_email or user_username

        if user:
            if not user.is_active:
                msg = 'User is inactive.'
                raise serializers.ValidationError(msg, code='authorization')

            refresh = self.get_token(user)

            data = dict()

            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

            update_last_login(None, user)

            return data

        else:
            msg = 'Unable to login with provided credentials.'
            raise serializers.ValidationError(msg, code='authorization')
