from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ApartmentViewSet, BuildingViewSet

_router = DefaultRouter()
_router.register("apartments", ApartmentViewSet)
_router.register("buildings", BuildingViewSet)

urlpatterns = [
    path("", include(_router.urls)),
    path("auth/", include("rest_framework.urls")),
]
