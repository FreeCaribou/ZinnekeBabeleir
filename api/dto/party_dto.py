from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField


class PartySimpleSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    logo = serializers.CharField(required=False)


class PartySerializer(PartySimpleSerializer):
    from api.dto.deputy_dto import DeputySimpleSerializer
    deputies = DeputySimpleSerializer(many=True, required=False)
