from rest_framework import permissions, viewsets

from api import models, serializers


class ApartmentViewSet(viewsets.ModelViewSet):
    # Commented out as Greg was too lazy to figure out token auth during setup
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.Apartment.objects.all()
    serializer_class = serializers.ApartmentSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer
