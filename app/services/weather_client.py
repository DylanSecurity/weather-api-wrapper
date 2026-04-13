import httpx
from fastapi import HTTPException
from app.core.config import settings

async def fetch_weather_from_api(city: str) -> dict:
    """
    Realiza la petición HTTP asíncrona a la API del clima externa.
    En este ejemplo usamos Visual Crossing.
    """
    # Construimos la URL. Usamos unitGroup=metric para que nos de grados Celsius.
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={settings.WEATHER_API_KEY}&contentType=json"
    
    # Abrimos un cliente HTTP asíncrono
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            
            # Si el código HTTP no es 200 (ej. 401 Unauthorized o 400 Bad Request), 
            # lanzamos un error que FastAPI capturará.
            response.raise_for_status()
            
            return response.json()
            
        except httpx.HTTPStatusError as exc:
            # Capturamos errores específicos del proveedor (ej. ciudad no encontrada)
            status_code = exc.response.status_code
            if status_code == 400:
                raise HTTPException(status_code=404, detail=f"Ciudad '{city}' no encontrada.")
            raise HTTPException(status_code=status_code, detail="Error en la API proveedora del clima.")
            
        except httpx.RequestError as exc:
            # Capturamos caídas de red (ej. la API externa está caída)
            raise HTTPException(status_code=503, detail="El servicio externo de clima no responde. Intente más tarde.")