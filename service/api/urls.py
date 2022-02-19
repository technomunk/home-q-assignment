from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ApartmentViewSet

_apartment_router = DefaultRouter()
_apartment_router.register("apartments", ApartmentViewSet)

urlpatterns = [
    path("", include(_apartment_router.urls)),
    path("auth/", include("rest_framework.urls")),
]
