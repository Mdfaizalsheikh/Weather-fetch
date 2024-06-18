import requests

API_KEY = 'bb8642ca964b1c2cdb2d47358e4b1d92'  
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

def display_weather(weather_data):
    if weather_data is None:
        print('Could not retrieve weather data.')
        return

    if weather_data.get('cod') != 200:
        print('Error:', weather_data.get('message'))
        return

    #print("Debug: Raw weather data:", weather_data)  # Debug line to print raw data

    main = weather_data.get('main', {})
    weather = weather_data.get('weather', [{}])[0]

    city_name = weather_data.get('name', 'Unknown')
    temperature = main.get('temp', 'Unknown')
    weather_description = weather.get('description', 'Unknown').capitalize()
    humidity = main.get('humidity', 'Unknown')
    pressure = main.get('pressure', 'Unknown')

    print(f"City: {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {weather_description}")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")

if __name__ == '__main__':
    city_name = input('Enter the city name: ')
    weather_data = get_weather(city_name)
    display_weather(weather_data)
