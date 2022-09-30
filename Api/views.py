from django.core import serializers as core_serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
import json


# @api_view(['POST'])
# @csrf_exempt
# def transalteToWolofServiceSingle(request):
#     codeLang = request.data['codeLang']
#     sentence = request.data['sentence']
    
#     result = translateToWolofSingle(codeLang, sentence)
#     res = json.dumps({"status":"200", "message":"TRANSLATION OK","type":"single" ,"result":result})
#     apiResponse = json.loads(res)
  
    
#     return Response(apiResponse, status=status.HTTP_201_CREATED)



# @api_view(['POST'])
# @csrf_exempt
# def transalteToWolofServiceMultiple(request):
#     codeLang = request.data['codeLang']
#     sentence = request.data['sentence']
#     output = request.data['output']
    
#     result = translateToWolofMultiple(codeLang, sentence, output)
#     res = json.dumps({"status":"200", "message":"TRANSLATION OK","type":"multiple" ,"result":result})
#     apiResponse = json.loads(res)
  
    
#     return Response(apiResponse, status=status.HTTP_201_CREATED)