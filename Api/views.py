from django.core import serializers as core_serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
import json
from .utils import *


@api_view(['POST'])
@csrf_exempt
def sentimentAnlysis(request):
    text = request.data['text']
    result = predictClass(text)
    res = json.dumps({"status":"200", "message":"API OK" ,"result":result})
    apiResponse = json.loads(res)

    return Response(apiResponse, status=status.HTTP_201_CREATED)


