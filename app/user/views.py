"""
Views for the user API.
"""

from rest_framework import generics, authentication, permissions
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.settings import api_settings
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

from user.serializers import (
    UserSerializer,
    MyTokenObtainPairSerializer,
    MyTokenRefreshSerializer
)



class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer

# class CreateTokenView(ObtainAuthToken):
#     """Create a new auth token for user"""
#     serializer_class = AuthTokenSerializer
#     renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class CustomTokenObtainPairView(generics.GenericAPIView):
    """Custom view for obtaining JWT token pair."""
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        """Handle POST request to obtain token pair."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class CustomTokenRefreshView(TokenRefreshView):
    """Custom view for refreshing JWT tokens."""
    serializer_class = MyTokenRefreshSerializer

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user