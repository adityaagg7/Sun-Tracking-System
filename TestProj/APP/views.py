from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
import requests
from django.http import HttpResponse
import WeatherForecast
import Prediction

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

@api_view('GET')
def sendPrediction(request):
    city=request.GET['city']
    list=WeatherForecast.get_weather(city)
    predicted_wattage=Prediction.predict_solar_power(list)
    return Response(predicted_wattage) 