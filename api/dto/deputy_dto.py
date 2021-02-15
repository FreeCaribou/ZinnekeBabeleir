from rest_framework import serializers


class DeputySimpleSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)


class DeputyWithPartySerializer(DeputySimpleSerializer):
    from api.dto.party_dto import PartySimpleSerializer
    party = PartySimpleSerializer()


class DeputySerializer(DeputyWithPartySerializer):
    from api.dto.vote_dto import VoteSimpleSerializer
    from api.dto.legislature_dto import LegislatureSimpleSerializer

    legislatures = LegislatureSimpleSerializer(many=True, required=False)
    votes = VoteSimpleSerializer(many=True, required=False)
