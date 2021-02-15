from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from api.services.home_service import error

from repository.repos import Party
from api.dto.party_dto import PartySerializer


def parties(request):
    data = Party.get_all()
    serializer = PartySerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


def party(request, party_id):
    try:
        data = Party.get_one(party_id)
    except:
        return error(request, 'This party doesnt exist')
    serializer = PartySerializer(data)
    return JsonResponse(serializer.data, safe=False)
