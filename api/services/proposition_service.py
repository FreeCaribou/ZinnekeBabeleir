from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from api.services.home_service import error

from repository.repos import Proposition
from api.dto.proposition_dto import PropositionSerializer


def propositions(request):
    data = Proposition.get_all()
    serializer = PropositionSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


def proposition(request, proposition_id):
    try:
        data = Proposition.get_one(proposition_id)
    except:
        return error(request, 'This proposition doesnt exist')
    serializer = PropositionSerializer(data)
    return JsonResponse(serializer.data, safe=False)
