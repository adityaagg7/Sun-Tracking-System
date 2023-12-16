from rest_framework.response import Response
from rest_framework.decorators import api_view



import requests
from django.http import HttpResponse

@api_view(['GET','POST']) 
def getVoltage(request):
    print(request)
    return Response("GOT DATA")
