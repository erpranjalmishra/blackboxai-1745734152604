from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx

router = APIRouter()

class HealthSuggestionRequest(BaseModel):
    user_input: str

GOOGLE_GEMINI_API_URL = "https://api.google.com/gemini/health"  # Placeholder URL
GOOGLE_GEMINI_API_KEY = "AIzaSyAcNuMyZIM2-bdCHD3UwCJCP_ezrB_FJaY"

@router.post("/health-suggestions")
async def get_health_suggestions(request: HealthSuggestionRequest):
    headers = {
        "Authorization": f"Bearer {GOOGLE_GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": request.user_input,
        "max_tokens": 100
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(GOOGLE_GEMINI_API_URL, json=payload, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to get health suggestions")
        data = response.json()
        return {"suggestions": data.get("choices", [{}])[0].get("text", "")}

@router.post("/chatbot")
async def chatbot_interaction(request: HealthSuggestionRequest):
    headers = {
        "Authorization": f"Bearer {GOOGLE_GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": request.user_input,
        "max_tokens": 150
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(GOOGLE_GEMINI_API_URL, json=payload, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to get chatbot response")
        data = response.json()
        return {"response": data.get("choices", [{}])[0].get("text", "")}
