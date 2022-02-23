from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

_router = DefaultRouter()
_router.register("apartments", views.ApartmentViewSet)
_router.register("persons", views.PersonViewSet)
_router.register("agreements", views.RentAgreementViewSet)
_router.register("buildings", views.BuildingViewSet)

urlpatterns = [
    path("", include(_router.urls)),
    path("auth/", include("rest_framework.urls")),
]
