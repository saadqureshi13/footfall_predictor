from datetime import date 
from footfall_predictor.services.weather_service import WeatherService
from footfall_predictor.services.holiday_service import HolidayService

class FootfallPredictor:
    def __init__(self):
        self.weather_service = WeatherService()
        self.holiday_service = HolidayService()
        
    async def predict(self, prediction_date: date):
        # Later replace this with real model & features
        weather = await self.weather_service.get_weather(prediction_date)
        holiday = await self.holiday_service.is_holiday(prediction_date)

        # simple dummy logic        
        base_visits = 120
        if holiday["is_holiday"]:
            base_visits -= 30

        prediction = base_visits + (20 if not weather["is_rainy"] else -20)

        return {
            "date": prediction_date,
            "predicted_visits": prediction,
            "confidence_interval": (prediction - 15, prediction + 15),
            "weather": weather,
            "holiday": holiday
        }