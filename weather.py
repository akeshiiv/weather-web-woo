import requests
from dataclasses import dataclass
from config import api_key

@dataclass
class WeatherData:
    main: str
    description: str 
    icon: str 
    temp: int


def get_lat_lon(city_name, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}').json()
    data = resp['coord']
    # resp[0] gets the 1st element of dict, aka 'coord'
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon

def get_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        main = resp.get('weather')[0].get('main'),
        description = resp.get('weather')[0].get('description'),
        icon = resp.get('weather')[0].get('icon'), 
        temp = int(resp.get('main').get('temp'))
        # remember to add comma after every variable definition! and also the string name of a dict should be within brackets
        )
    return data

def main(city_name):
    lat, lon = get_lat_lon(city_name, api_key)
    weather = get_weather(lat, lon, api_key)
    return weather

    # check u converted url to json. or else it wont become a dictionary and you'll get an attributeError.
