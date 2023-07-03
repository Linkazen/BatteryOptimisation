import requests
from requests.auth import HTTPBasicAuth
import datetime
import json

import APIKeys


def GetTariffInfo():
    Period_from = datetime.datetime.now().replace(hour=22, minute=0, second=0, microsecond=0).isoformat() + "Z"
    TariffInfo = requests.get(f"https://api.octopus.energy/v1/products/{APIKeys.Product_Code}/electricity-tariffs/{APIKeys.Tariff_Code}/standard-unit-rates?period_from={Period_from}")
    
    with open("/home/pi/BatteryOptimisation/InverterInfo/Tariffs.json", "w") as TariffFile:
        TariffFile.write(json.dumps(TariffInfo.json()))

"""
In order to save API calls the function
will save the information to a json file
in order to be used elsewhere in the program
"""
def GetWeatherInfo():
    WeatherInfo = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={APIKeys.lat}&lon={APIKeys.lon}&appid={APIKeys.WeatherKey}")

    with open("InverterInfo/WeatherForecast.json", "w") as WeatherFile:
        WeatherFile.write(json.dumps(WeatherInfo.json()))

GetTariffInfo()