from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
from Modules import WeatherForecast
from Modules import Prediction
from APP.models import Voltage

@api_view(['GET', 'POST'])
def receiveESPData(request):
    rv=0
    sv=0
    if request.method == 'POST':
        sv=request.POST['SVoltage']
        rv=request.POST['RVoltage']
    else:
        sv=request.GET['SVoltage']
        rv=request.GET['RVoltage']
    Voltage.objects.create(s_voltage=sv, r_voltage=rv)
    return Response("GOT DATA")


@api_view(['GET'])
def sendVoltage(request):
    # num = round(random.uniform(0, 10), 2)
    v=Voltage.objects.latest('time')
    # v=1
    return Response({'staticVoltage':v.s_voltage,'rotationalVoltage':v.r_voltage})


@api_view(['GET'])
def sendPrediction(request):
    city = request.GET['city']
    parameters = WeatherForecast.get_weather(city)
    predicted_wattage = Prediction.predict_solar_power(parameters)

    return Response(predicted_wattage)
