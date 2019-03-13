from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from rest_api.serializers import StatsSerializer


@api_view(["GET"])
def api_version(request):
    api_version = {"api_version": "0.1"}
    return JsonResponse(api_version, status=200)


@api_view(["POST"])
def stats(request):
    data = JSONParser().parse(request)
    serializer = StatsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
