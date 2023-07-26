import weather_api
import weather_analyzer

if __name__ == '__main__':
    api_key = 'c4b3f5cf716b4d4a2db2c07291469c18'
    city = input("Enter a city name: ").strip().lower()

    weather_data = weather_api.get_weather_data(api_key, city)
    city = weather_analyzer.display_weather(weather_data)
    weather_analyzer.plot_weather(weather_data, city)



