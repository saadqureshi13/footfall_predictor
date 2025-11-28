from pydantic import BaseModel
from datetime import date

class WeatherInfo(BaseModel):
    date: date
    temp_max: float
    temp_min: float
    precipitation: float
    is_rainy: bool

class PredictionResponse(BaseModel):
    date: date
    predicted_visits: int
    confidence_interval: tuple[int, int]
    weather: WeatherInfo