"""
Serializers for the user API View.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate
)
from django.utils.translation import gettext as _

from rest_framework import serializers

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer
    )




class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return the user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom JWT token serializer."""
    @classmethod
    def get_token(cls, user):
        """Get token for the user."""
        token = super().get_token(user)

        token['email'] = user.email
        token['name'] = user.name
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data['user_name'] = self.user.name
        data['user_email'] = self.user.email
        return data


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    """Custom serializer for token refresh."""
    refresh = serializers.CharField()

    def validate(self, attrs):
        """Validate the refresh token."""
        data = super().validate(attrs)
        return data


# class AuthTokenSerializer(serializers.Serializer):
#     """Serializer for the user auth token,"""
#     email = serializers.EmailField()
#     password = serializers.CharField(
#         style={'input_type': 'password'},
#         trim_whitespace=False
#     )

#     def validate(self, attrs):
#         """Validate and authenticate the user"""
#         email = attrs.get('email')
#         password = attrs.get('password')
#         user = authenticate(
#             request=self.context.get('request'),
#             username=email,
#             password=password
#         )
#         if not user:
#             msg = _('Unable to authenticate with provided credentials.')
#             raise serializers.ValidationError(msg, code='authentication')

#         attrs['user'] = user
#         return attrs
