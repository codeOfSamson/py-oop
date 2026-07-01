import os
from dotenv import load_dotenv
import datetime as dt
import requests as rq
from pprint import pprint
from parser import parse_forecast
import pandas as pd
from scheduler import Scheduler # type: ignore

load_dotenv()

class WeatherFetcher:

    def __init__(self, url:str, api_key:str):
        self.url = self.construct_full_url(url, api_key )
        self._data = None

    @staticmethod
    def construct_full_url(url:str, api_key) -> str:
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
            return parse_forecast(self.raw_data)
        return []
          
#############

class DataStorage:
    def __init__(self, name_prefix:str):
        self.name_prefix = name_prefix

    def create_dataframe(self, data:list)->pd.DataFrame:
        return pd.DataFrame(data)


#############

class WeatherScheduler:
    name_prefix = 'my_records'
    def __init__(self, seconds: int, weather_details: list[str]):
        self.schedule = Scheduler()
        self.schedule.cyclic(dt.timedelta(seconds=seconds), self.orchestrate)
        self.weather_instance = WeatherFetcher(*weather_details)
        self.data_storage = DataStorage(WeatherScheduler.name_prefix)

    def orchestrate(self):
        data = self.weather_instance.raw_data
        data_frames = self.data_storage.create_dataframe(data)
        print(data_frames)

    def run(self):
        while True:
            self.schedule.exec_jobs()

#############

api_key = os.getenv("api_key")

url= "https://my.meteoblue.com/packages/basic-1h,basic-3h,basic-day?lat=48&lon=8&tz=UTC&apikey=YOUR_APIKEY"
# weather_instance = WeatherFetcher(url, "ntqbypuLOiFgVCA4")
# pprint(weather_instance.cleaned_data)
scheduler_instance = WeatherScheduler(1,[url, api_key]).run()


        