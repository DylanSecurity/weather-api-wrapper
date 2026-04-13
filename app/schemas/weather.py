from pydantic import BaseModel

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    conditions: str
    description: str