from rest_framework import serializers


class PartySimpleSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=100)


class PartySerializer(PartySimpleSerializer):
    from api.dto.deputy_dto import DeputySimpleSerializer
    deputies = DeputySimpleSerializer(many=True, required=False)
