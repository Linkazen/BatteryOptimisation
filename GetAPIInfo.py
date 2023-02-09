import requests
from requests.auth import HTTPBasicAuth
import json

import APIKeys


def GetTariffInfo():
    TariffFile = open("InverterInfo/Tariffs.json", "w")

    TariffInfo = requests.get(f"https://api.octopus.energy/v1/products/{APIKeys.Product_Code}/electricity-tariffs/{APIKeys.Tariff_Code}/standard-unit-rates/")

    TariffFile.write(json.dumps(TariffInfo.json()))
    TariffFile.close()


def GetWeatherInfo():
    WeatherFile = open("InverterInfo/WeatherForecast")

    WeatherInfo = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={APIKeys.lat}&lon={APIKeys.lon}&appid={APIKeys.WeatherKey}")

GetTariffInfo()