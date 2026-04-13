# 🌤️ Weather API Wrapper

A high-performance, containerized API wrapper built with **FastAPI** and **Redis** that retrieves weather data while optimizing network requests through aggressive caching.

## 🚀 Architecture & Features

- **Framework:** FastAPI (Python 3.11)
- **Caching Layer:** Redis (In-memory data store)
- **External API:** Visual Crossing Weather
- **Data Validation:** Pydantic

### 🧠 Engineering Decisions
1. **Reduced Latency & Costs:** Implemented a Redis caching layer (12-hour TTL). Subsequent requests for the same city return in milliseconds without hitting the external provider, preventing rate-limit blocks.
2. **Asynchronous I/O:** Utilized `httpx` and `redis.asyncio` to prevent blocking the main server thread during external network calls.
3. **Isolated Environments:** Fully containerized the application and database using Docker Compose, ensuring a "works on my machine, works in production" standard.

## 📂 Project Structure

```text
weather-api-wrapper/
├── app/
│   ├── api/              # Route handlers (Controllers)
│   ├── core/             # App configurations and secrets
│   ├── schemas/          # Pydantic models (Data contracts)
│   └── services/         # Business logic (External API & Cache)
├── main.py               # Application entry point
├── Dockerfile            # Container recipe
├── docker-compose.yml    # Infrastructure orchestrator
└── requirements.txt      # Python dependencies
```

## 🛠️ How to Run (Local Development)

### Prerequisites
- Docker and Docker Compose installed.
- A free API key from [Visual Crossing](https://www.visualcrossing.com/weather-api).

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/weather-api-wrapper.git
   cd weather-api-wrapper
   ```

2. **Set up environment variables:**
   Rename the `.env.example` file to `.env` and insert your API key.
   ```env
   WEATHER_API_KEY=your_actual_api_key_here
   REDIS_URL=redis://redis_cache:6379/0
   ```

3. **Build and start the containers:**
   ```bash
   docker-compose up --build -d
   ```

## 📡 API Endpoints

Once the container is running, you can access the interactive Swagger UI at: `http://127.0.0.1:8000/docs`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Application health check. |
| `GET` | `/weather/{city}` | Retrieves cached or live weather data for a city. |

### Example Request
```bash
curl -X GET "http://127.0.0.1:8000/weather/santiago"
```

### Example Response
```json
{
  "city": "Santiago",
  "temperature": 25.4,
  "conditions": "Clear",
  "description": "Clear conditions throughout the day."
}
```

## 🛑 Stopping the Application
To gracefully stop and remove the containers and network, run:
```bash
docker-compose down
```
