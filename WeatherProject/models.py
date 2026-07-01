from dataclasses import dataclass
from datetime import datetime

@dataclass
class HourlyWeather:
    time: datetime
    temperature: float
    feels_like: float
    humidity: int
    windspeed: float
    winddirection: int
    precipitation: float
    precipitation_probability: int
    pressure: float
    uv_index: int
    is_daylight: bool

@dataclass
class Forecast:
    latitude: float
    longitude: float
    timezone: str
    hourly: list[HourlyWeather]