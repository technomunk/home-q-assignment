from rest_framework import serializers as rest_serializers

from api import models


class ApartmentSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.Apartment
        fields = [
            "id",
            "city",
            "street",
            "street_number",
            "rooms",
            "floor",
            "area",
            "rent",
            "description",
        ]
