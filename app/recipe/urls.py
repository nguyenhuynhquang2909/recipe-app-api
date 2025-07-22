"""
URL mapping for the recipe app.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet, basename='recipe')
router.register('tags', views.TagViewSet, basename='tag')

app_name = 'recipe'


urlpatterns = [
    path('', include(router.urls)),
]