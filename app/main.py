from fastapi import FastAPI
from app.api import weather # Importamos la carpeta api

app = FastAPI(
    title="Weather API Wrapper",
    description="Servicio de clima optimizado con caché",
    version="1.0.0"
)

# Conectamos las rutas del clima
app.include_router(weather.router, prefix="/weather", tags=["Weather"])

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "El servicio está operativo"}