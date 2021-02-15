from django.http import HttpResponse, JsonResponse
from rest_framework import serializers


# TODO better
class ErrorSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)


# TODO better
def error(request, message):
    print('raise error', message)
    data = {'message': message}
    serializer = ErrorSerializer(data)
    return JsonResponse(serializer.data, safe=False, status=400)
