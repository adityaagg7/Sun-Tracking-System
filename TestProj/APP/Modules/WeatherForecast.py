import requests

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key=&q=${city}&aqi=no`;"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        barometer=data['current']['pressure_mb']
        temp=data['current']['temp_c']
        wind=data['current']['wind_kph']
        humidity=data['current']['humidity']
        weather=data['current']['condition']['text']
    else:
        return "Error occured"