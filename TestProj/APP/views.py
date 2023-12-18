from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
from Modules import WeatherForecast
from Modules import Prediction
from APP.models import Voltage

@api_view(['GET', 'POST'])
def receiveESPData(request):
    v=0
    if request.method == 'POST':
        v=request.POST['Voltage']
    else:
        v=request.GET['Voltage']
    Voltage.objects.create(voltage=v)
    return Response("GOT DATA")


@api_view(['GET'])
def sendVoltage(request):
    # num = round(random.uniform(0, 10), 2)
    v=Voltage.objects.latest('time')
    # v=1
    return Response({'volt':v.voltage})


@api_view(['GET'])
def sendPrediction(request):
    city = request.GET['city']
    parameters = WeatherForecast.get_weather(city)
    predicted_wattage = Prediction.predict_solar_power(parameters)

    return Response(predicted_wattage)
