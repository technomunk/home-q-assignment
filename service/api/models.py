from django.db import models

from .utils import get_current_date, get_date_in_30_days


class Building(models.Model):
    # rely on auto-generated "id" field for pk

    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    street_number = models.CharField(max_length=16)

    description = models.TextField(blank=True, default="")


class Apartment(models.Model):
    # rely on auto-generated "id" field for pk

    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    street_number = models.CharField(max_length=16)
    rooms = models.IntegerField()
    floor = models.IntegerField()
    area = models.IntegerField()
    rent = models.IntegerField()

    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)

    description = models.TextField(blank=True, default="")
    building = models.ForeignKey(
        Building,
        related_name="apartments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


class Person(models.Model):
    # rely on auto-generated "id" field for pk

    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    # other contact info should also be part of this model


class RentAgreement(models.Model):
    apartment = models.OneToOneField(
        Apartment,
        on_delete=models.CASCADE,
        primary_key=True,  # Note: makes switching to many-to-one relationship significantly harder in the future
    )

    lender = models.ForeignKey(
        Person,
        related_name="lender_agreements",
        on_delete=models.CASCADE,
    )
    tenant = models.ForeignKey(
        Person,
        related_name="tenant_agreements",
        on_delete=models.CASCADE,
    )

    start_date = models.DateField(default=get_current_date)
    end_date = models.DateField(default=get_date_in_30_days)
