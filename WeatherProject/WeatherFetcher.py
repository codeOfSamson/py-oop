import os
import requests as rq
from pprint import pprint
from parser import parse_forecast


class WeatherFetcher:

    def __init__(self, url:str, api_key:str):
        self.url = self.construct_full_url(url, api_key )
        self._data = None

    @staticmethod
    def construct_full_url(url:str, api_key) -> str:
        print(f"here{api_key}")
        return url.replace("YOUR_APIKEY", api_key)
    
    @property
    def raw_data(self)-> dict:
        if self._data is None:
            response = rq.get(self.url)
            self._data = response.json()
            return self._data
        
    @property
    def cleaned_data(self) -> list:
        if self.raw_data:
            self.cleaned_data = parse_forecast(self.raw_data)
          


api_key = os.getenv("api_key")

url= "https://my.meteoblue.com/packages/basic-1h,basic-3h,basic-day?lat=48&lon=8&tz=UTC&apikey=YOUR_APIKEY"
weather_instance = WeatherFetcher(url, "ntqbypuLOiFgVCA4")
pprint(weather_instance.cleaned_data)
