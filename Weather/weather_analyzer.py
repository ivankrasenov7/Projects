import matplotlib.pyplot as plt

def display_weather(weather_data):
    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        weather_desc = weather_data["weather"][0]["description"]

        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_desc}")

        city = weather_data["name"]
        return city
    else:
        print("City not found")

def plot_weather(weather_data, city):
    main_data = weather_data["main"]
    temperature = main_data["temp"]
    humidity = main_data["humidity"]

    labels = ["Temperature", "Humidity"]
    values = [temperature, humidity]
    plt.bar(labels, values, color=["blue", "orange"])
    plt.xlabel("Weather Parameter")
    plt.ylabel("Value")
    plt.title(f"Weather in {city.capitalize()}")

    weather_conditions = ["Clear", "Clouds", "Rain", "Thunderstorm", "Snow"]
    condition_counts = [0] * len(weather_conditions)

    for weather in weather_data["weather"]:
        if weather["main"] == "Clear":
            condition_counts[0] += 1
        elif weather["main"] == "Clouds":
            condition_counts[1] += 1
        elif weather["main"] == "Rain":
            condition_counts[2] += 1
        elif weather["main"] == "Thunderstorm":
            condition_counts[3] += 1
        elif weather["main"] == "Snow":
            condition_counts[4] += 1

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.pie(condition_counts, labels=weather_conditions, autopct='%1.1f%%',
            colors=["green", "gray", "blue", "yellow", "white"])
    plt.title("Weather Conditions Distribution")

    plt.subplot(1, 2, 2)
    plt.bar(labels, values, color=["blue", "orange"])
    plt.xlabel("Weather Parameter")
    plt.ylabel("Value")
    plt.title(f"Weather in {city.capitalize()}")

    plt.tight_layout()
    plt.show()
