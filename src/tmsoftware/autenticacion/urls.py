from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngenieroViewSet


router = DefaultRouter()
router.register(r'ingenieros', IngenieroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]