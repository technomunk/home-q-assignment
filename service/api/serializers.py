from rest_framework import serializers as rest_serializers

from api import models


class ApartmentSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.Apartment
        fields = "__all__"
        read_only_fields = ["id"]


class BuildingSerializer(rest_serializers.ModelSerializer):
    apartments = rest_serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Building
        fields = "__all__"
        read_only_fields = ["id"]
