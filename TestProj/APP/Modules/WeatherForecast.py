import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv() 
WEATHER= str(os.getenv('WEATHER'))

import requests

def get_weather_forecast( location, days=6, aqi="no", alerts="no"):
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": WEATHER,
        "q": location,
        "days": days,
        "aqi": aqi,
        "alerts": alerts
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        # Extract forecast information for each day
        forecast_dict = {}

        # Extract forecast information for each day
        for day_forecast in weather_data["forecast"]["forecastday"]:
            date = day_forecast["date"]
            avg_temp_c = day_forecast["day"]["avgtemp_c"]
            max_wind_kph = day_forecast["day"]["maxwind_kph"]
            avg_humidity = day_forecast["day"]["avghumidity"]
            condition_text = day_forecast["day"]["condition"]["text"]

            # Create a dictionary for each date
            date_info = {
                "temp": avg_temp_c,
                "wind": max_wind_kph,
                "humidity": avg_humidity,
                "weather": condition_text
            }

            # Add the date information to the main forecast dictionary
            forecast_dict[date] = date_info

        return forecast_dict
    else:
        print(f"Error: Unable to fetch weather data. Status Code: {response.status_code}")
