from rest_framework.viewsets import ModelViewSet

from api import models, serializers


class ApartmentViewSet(ModelViewSet):
    queryset = models.Apartment.objects.all()
    serializer_class = serializers.ApartmentSerializer
