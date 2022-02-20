from rest_framework import serializers as rest_serializers

from api import models


class ApartmentSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.Apartment
        fields = "__all__"
        read_only_fields = ["id"]


class BuildingSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.Building
        fields = "__all__"
        read_only_fields = ["id"]

    apartments = rest_serializers.PrimaryKeyRelatedField(queryset=models.Apartment.objects.all(), many=True)


class BuildingWithApartmentsSerializer(BuildingSerializer):
    apartments = ApartmentSerializer(many=True)


class PersonSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = "__all__"
        read_only_fields = ["id"]


class RentAgreementSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.RentAgreement
        fields = "__all__"
