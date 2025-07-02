"""
URL mappings for the user API.
"""
from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', views.CustomTokenRefreshView.as_view(), name='token-refresh'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]