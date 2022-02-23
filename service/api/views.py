from rest_framework import permissions, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

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

    def retrieve(self, request: Request, pk: int, **kwargs):
        queryset = models.Building.objects.get(id=pk)
        serializer = serializers.BuildingWithApartmentsSerializer(queryset)
        return Response(serializer.data)


class PersonViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class RentAgreementViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.RentAgreement.objects.all()
    serializer_class = serializers.RentAgreementSerializer
