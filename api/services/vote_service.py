from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from api.services.home_service import error

from repository.repos import Vote
from api.dto.vote_dto import VoteSerializer


def votes(request):
    data = Vote.get_all()
    serializer = VoteSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)
