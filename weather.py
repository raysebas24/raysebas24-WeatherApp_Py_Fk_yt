import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

# pull data from file .env
load_dotenv()
api_key = os.getenv('API_KEY')    # crap API_KEY from file

# with '@dataclass' you dont need '__init__' and '__repr__' and '__eq__' method
@dataclass
class WeatherData:
    print("[WeatherDate] - call successful")
    main: str
    decscription: str
    icon: str
    temperature: int


# give me location information
def get_lan_lon(city_name, state_code, country_code, API_key):
    print("[get_lan_lon] - call successful")
    resp = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()    #c consert response into valid json
    data = resp[0]
    lat , lon = data.get('lat'), data.get('lon')
    return lat, lon


# give me the location weather data
def get_current_weather(lat, lon, API_key):
    print("[get_current_weather] - call successful")
    resp = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()    # gibe me back the weather data of the specific location
    data = WeatherData(
        main=resp.get('weather')[0].get('main'),
        decscription=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temperature=int(resp.get('main').get('temp'))
    )
    return data


def main(city_name, state_name, country_name):
    print("[main] - call successful")
    lat, lon = get_lan_lon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data


if __name__ == "__main__":
    print("[weather.py - call successful]")
    lat, lon = get_lan_lon('Toronto', 'ON', 'Canada', api_key)
    print("[get_current_weather(lat, lon, api_key)]: ", get_current_weather(lat, lon, api_key))