from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KPIViewSet, AssetKPIViewSet

router = DefaultRouter()
router.register('kpis', KPIViewSet)
router.register('asset-kpis', AssetKPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
