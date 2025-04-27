from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

WEATHER_API_KEY = "your_openweather_api_key_here"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

@router.get("/weather")
async def get_weather(city: str):
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(WEATHER_API_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch weather data")
        data = response.json()
        return {
            "city": data.get("name"),
            "temperature": data.get("main", {}).get("temp"),
            "description": data.get("weather", [{}])[0].get("description"),
            "humidity": data.get("main", {}).get("humidity"),
            "wind_speed": data.get("wind", {}).get("speed")
        }
