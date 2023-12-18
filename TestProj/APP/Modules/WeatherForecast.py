import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv() 
WEATHER= str(os.getenv('WEATHER'))
def get_weather(city):
    print(WEATHER)
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER}&q=${city}&aqi=no`;"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        barometer = data['current']['pressure_mb']
        temp = data['current']['temp_c']
        wind = data['current']['wind_kph']
        humidity = data['current']['humidity']
        weather = data['current']['condition']['text']
        current_date = datetime.now().strftime('%Y-%m-%d')
        parameters = { "temp": temp, "weather": weather, "wind": wind, "humidity": humidity,"date":current_date}
        return parameters
    else:
        return "Error occurred"
