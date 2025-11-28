from datetime import date
import httpx

class WeatherService:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    async def get_weather(self, target_date: date) -> dict:
        """
        Returns mock weather data for Berlin.
        Later: connect this to a real weather API or dataset.
        """
        params = {
            "latitude": 52.52,   # Berlin latitude
            "longitude": 13.41,  # Berlin longitude
            "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
            "timezone": "Europe/Berlin",
            "start_date": target_date.isoformat(),
            "end_date": target_date.isoformat(),
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

        daily= data['daily']
        weather = {
            'date': target_date.isoformat(),
            'temp_max': daily['temperature_2m_max'][0],
            'temp_min': daily['temperature_2m_min'][0],
            'precipitation': daily['precipitation_sum'][0],
            'is_rainy': daily['precipitation_sum'][0] > 1.0
        }
        return weather
