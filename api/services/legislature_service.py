from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from api.services.home_service import error

from repository.repos import Legislature
from api.dto.legislature_dto import LegislatureSerializer


def legislatures(request):
    data = Legislature.get_all()
    serializer = LegislatureSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)
