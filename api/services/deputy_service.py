from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from api.services.home_service import error

from repository.repos import Deputy
from api.dto.deputy_dto import DeputySerializer


def deputies(request):
    data = Deputy.get_all()
    serializer = DeputySerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


def deputy(request, deputy_id):
    try:
        data = Deputy.get_one(deputy_id)
    except:
        return error(request, 'This deputy doesnt exist')
    serializer = DeputySerializer(data)
    return JsonResponse(serializer.data, safe=False)
