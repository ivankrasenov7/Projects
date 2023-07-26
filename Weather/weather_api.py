import requests
import json

def get_weather_data(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    weather_data = json.loads(response.text)
    return weather_data
