from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NetworkNodeViewSet

router = DefaultRouter()
router.register(r'nodes', NetworkNodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
