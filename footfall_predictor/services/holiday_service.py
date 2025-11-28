import httpx
from datetime import date

class HolidayService:
    BASE_URL = "https://date.nager.at/api/v3/PublicHolidays"

    async def is_holiday(self, target_date: date) -> dict:
        """Check if the given date is a public holiday in Germany"""
        year = target_date.year
        url = f"{self.BASE_URL}/{year}/DE"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            holidays = response.json()

        for holiday in holidays:
            if holiday["date"] == target_date.isoformat():
                return {
                    "is_holiday": True,
                    "local_name": holiday["localName"],
                    "name": holiday["name"]
                }

        return {"is_holiday": False}

