from rest_framework import serializers


class LegislatureSimpleSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    begin_date = serializers.DateField()
    end_date = serializers.DateField()
    parliament = serializers.CharField(max_length=10)


class LegislatureSerializer(LegislatureSimpleSerializer):
    from api.dto.deputy_dto import DeputySimpleSerializer, DeputyWithPartySerializer
    deputies = DeputyWithPartySerializer(many=True, required=False)
