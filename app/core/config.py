from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Weather API Wrapper"
    WEATHER_API_KEY: str
    REDIS_URL: str # ¡Agregamos esta línea!

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()