# 🌤️ Weather API Wrapper | Made with AI

A high-performance, containerized API wrapper built with **FastAPI** and **Redis** that retrieves weather data while optimizing network requests through aggressive caching and rate limiting considerations.

## 🚀 Architecture & Tech Stack

- **Framework:** FastAPI (Python 3.11)
- **Caching Layer:** Redis (In-memory data store to minimize third-party API calls)
- **External API:** Visual Crossing Weather
- **Infrastructure:** Docker & Docker Compose
- **Data Validation:** Pydantic

## 🧠 Engineering Decisions

1. **Reduced Latency & Costs:** Implemented a Redis caching layer (12-hour TTL). Subsequent requests for the same city return in milliseconds without hitting the external provider, preventing rate-limit blocks and reducing latency.
2. **Asynchronous I/O:** Utilized `httpx` and `redis.asyncio` to prevent blocking the main server thread during external network calls.
3. **Isolated Environments:** Fully containerized the application and database using Docker Compose, ensuring a "works on my machine, works in production" standard.
4. **Data Contracts:** Used Pydantic schemas to sanitize and standardize the chaotic payload from the external provider into a clean, predictable JSON response.

## 🛠️ How to Run (Local Development)

### Prerequisites
- Docker and Docker Compose installed.
- A free API key from [Visual Crossing](https://www.visualcrossing.com/weather-api).

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/weather-api-wrapper.git](https://github.com/YOUR_USERNAME/weather-api-wrapper.git)
   cd weather-api-wrapper
