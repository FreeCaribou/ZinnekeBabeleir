from rest_framework import serializers


class VoteSimpleSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    type_code = serializers.CharField()


class VoteSerializer(VoteSimpleSerializer):
    from api.dto.deputy_dto import DeputySimpleSerializer
    deputy = DeputySimpleSerializer()
