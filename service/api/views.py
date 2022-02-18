from logging import getLogger

from django.http import HttpRequest, JsonResponse
from django.views import View

from .models import Apartment

_logger = getLogger(__name__)


class ApartmentsView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        apartments = Apartment.objects.all()
        serialized_data = [apartment.serialize() for apartment in apartments]
        return JsonResponse(serialized_data, safe=False)
