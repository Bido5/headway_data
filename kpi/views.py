from rest_framework import viewsets
from .models import KPI, AssetKPI
from .serializers import KPISerializer, AssetKPISerializer

class KPIViewSet(viewsets.ModelViewSet):
    queryset = KPI.objects.all()
    serializer_class = KPISerializer

class AssetKPIViewSet(viewsets.ModelViewSet):
    queryset = AssetKPI.objects.all()
    serializer_class = AssetKPISerializer
