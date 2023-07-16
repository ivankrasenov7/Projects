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

def display_weather(weather_data):
    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        weather_desc = weather_data["weather"][0]["description"]

        print(f"Temperature{temperature}")
        print(f"Humidity: {humidity}")
        print(f"Weather: {weather_desc}")
    else:
        print("City not found")

if __name__ == '__main__':
    api_key = 'c4b3f5cf716b4d4a2db2c07291469c18'
    city = input("Enter a city name: ").strip().lower()
    weather_data = get_weather_data(api_key, city)
    display_weather(weather_data)


