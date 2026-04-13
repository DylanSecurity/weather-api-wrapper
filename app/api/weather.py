from fastapi import APIRouter, HTTPException
from app.services.weather_client import fetch_weather_from_api
from app.services.cache import get_cached_weather, set_weather_cache
from app.schemas.weather import WeatherResponse

router = APIRouter()

@router.get("/{city}", response_model=WeatherResponse)
async def get_weather(city: str):
    # 1. Intentar obtener de la caché (Redis)
    cached_data = await get_cached_weather(city)
    
    if cached_data:
        # ¡Cache Hit! Retornamos de inmediato
        # Agregamos un log interno para saber que vino de Redis
        print(f"DEBUG: Cache Hit para {city}")
        return WeatherResponse(**cached_data)

    # 2. Cache Miss: Ir a la API externa
    print(f"DEBUG: Cache Miss para {city}. Llamando a API externa...")
    raw_data = await fetch_weather_from_api(city)
    
    try:
        current = raw_data.get("currentConditions", {})
        
        # Preparamos la respuesta limpia
        weather_data = {
            "city": raw_data.get("address", city).title(),
            "temperature": current.get("temp", 0.0),
            "conditions": current.get("conditions", "Desconocido"),
            "description": raw_data.get("description", "Sin descripción")
        }

        # 3. Guardar en caché para la próxima vez
        await set_weather_cache(city, weather_data)

        return WeatherResponse(**weather_data)
        
    except Exception:
        raise HTTPException(status_code=500, detail="Error procesando datos.")