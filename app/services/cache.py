import json
from redis import asyncio as aioredis
from app.core.config import settings

# Inicializamos el cliente de Redis
# El pool de conexiones gestiona eficientemente múltiples peticiones
redis_client = aioredis.from_url(settings.REDIS_URL, decode_responses=True)

async def get_cached_weather(city: str) -> dict | None:
    """Intenta obtener el clima desde Redis usando la ciudad como llave."""
    try:
        data = await redis_client.get(city.lower())
        if data:
            return json.loads(data)
    except Exception:
        # En producción, aquí loguearíamos el error
        return None
    return None

async def set_weather_cache(city: str, data: dict, expire: int = 43200):
    """Guarda los datos en Redis con un tiempo de expiración (TTL)."""
    try:
        # 43200 segundos = 12 horas
        await redis_client.set(city.lower(), json.dumps(data), ex=expire)
    except Exception:
        pass # Fallo silencioso para no interrumpir el flujo