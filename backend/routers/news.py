from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

NEWS_API_KEY = "your_news_api_key_here"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

@router.get("/health-news")
async def get_health_news(country: str = "us", category: str = "health"):
    params = {
        "apiKey": NEWS_API_KEY,
        "country": country,
        "category": category,
        "pageSize": 10
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(NEWS_API_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch news")
        data = response.json()
        return data.get("articles", [])
