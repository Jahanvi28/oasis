import requests

def get_weather(api_key, location):
    """
    Get current weather data for a specified location using the OpenWeatherMap API.

    :param api_key: OpenWeatherMap API key
    :param location: City name or ZIP code
    :return: Weather data (temperature, humidity, and weather conditions)
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "conditions": data["weather"][0]["description"],
            }
            return weather_info
        else:
            print(f"Error: {data['message']}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    print("Command-line Weather App")
    print("------------------------")

    api_key = input("Enter your OpenWeatherMap API key: ")
    location = input("Enter the city name or ZIP code: ")

    weather_data = get_weather(api_key, location)

    if weather_data:
        print("\nCurrent Weather:")
        print("----------------")
        print(f"Location: {location}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Conditions: {weather_data['conditions']}")
    else:
        print("Unable to fetch weather data. Please check your input and API key.")

if __name__ == "__main__":
    main()
