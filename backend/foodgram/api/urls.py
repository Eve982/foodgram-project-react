from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewSet

from .views import IngredientViewSet, RecipeViewSet, TagViewSet

app_name = 'api'

router = DefaultRouter()

router.register('users', CustomUserViewSet)
router.register('recipes', RecipeViewSet)
router.register('ingredients', IngredientViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
]
