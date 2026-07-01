from datetime import datetime
from models import Forecast, HourlyWeather

def parse_forecast(data: dict) -> Forecast:
    meta = data["metadata"]
    h = data["data_1h"]

    hourly = [
        HourlyWeather(
            time=datetime.strptime(h["time"][i], "%Y-%m-%d %H:%M"),
            temperature=h["temperature"][i],
            feels_like=h["felttemperature"][i],
            humidity=h["relativehumidity"][i],
            windspeed=h["windspeed"][i],
            winddirection=h["winddirection"][i],
            precipitation=h["precipitation"][i],
            precipitation_probability=h["precipitation_probability"][i],
            pressure=h["sealevelpressure"][i],
            uv_index=h["uvindex"][i],
            is_daylight=bool(h["isdaylight"][i]),
        )
        for i in range(len(h["time"]))
    ]

    return Forecast(
        latitude=meta["latitude"],
        longitude=meta["longitude"],
        timezone=meta["timezone_abbrevation"],
        hourly=hourly,
    )