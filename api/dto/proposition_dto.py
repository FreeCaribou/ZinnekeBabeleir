from rest_framework import serializers


class PropositionSimpleSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    date = serializers.DateField()
    vote_count = serializers.IntegerField(required=False)
    vote_for = serializers.IntegerField(required=False)
    vote_against = serializers.IntegerField(required=False)
    vote_abstention = serializers.IntegerField(required=False)
    vote_absent = serializers.IntegerField(required=False)


class PropositionSerializer(PropositionSimpleSerializer):
    from api.dto.legislature_dto import LegislatureSimpleSerializer
    from api.dto.vote_dto import VoteSerializer
    legislature = LegislatureSimpleSerializer()
    votes = VoteSerializer(many=True, required=False)
