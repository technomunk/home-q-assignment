from django.db import models


class Building(models.Model):
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    street_number = models.CharField(max_length=16)

    description = models.TextField(default="")


class Apartment(models.Model):
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    street_number = models.CharField(max_length=16)
    rooms = models.IntegerField()
    floor = models.IntegerField()
    area = models.IntegerField()
    rent = models.IntegerField()

    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)

    description = models.TextField(default="")
    building = models.ForeignKey(
        Building,
        related_name="apartments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


from django.contrib import admin

admin.register(Building)
admin.register(Apartment)
