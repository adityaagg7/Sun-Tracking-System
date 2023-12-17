from rest_framework.response import Response
from rest_framework.decorators import api_view
import random


import requests
from django.http import HttpResponse

@api_view(['GET','POST']) 
def receiveESPData(request):
    if request.method=='POST':
        print(request.POST['Voltage'])
    else:
        print(request.GET['Voltage'])
    return Response("GOT DATA")


@api_view(['GET'])
def sendVoltage(request):
    num = round(random.uniform(0, 10), 2)
    return Response(num)


@api_view(['GET'])
def sendCurrent(request):
    num = round(random.uniform(0, 1), 3)
    return Response(num)
