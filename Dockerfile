# 1. Usamos una versión oficial y ligera de Python
FROM python:3.11-slim

# 2. Le decimos a Docker en qué carpeta interna va a trabajar
WORKDIR /app

# 3. Copiamos el archivo de requerimientos primero (para aprovechar el caché de Docker)
COPY requirements.txt .

# 4. Instalamos las librerías sin guardar archivos temporales
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos todo el código de nuestra aplicación a la carpeta /app del contenedor
COPY . .

# 6. Exponemos el puerto donde correrá Uvicorn
EXPOSE 8000

# 7. El comando para encender el servidor. 
# Nota el --host 0.0.0.0, es vital en Docker para que acepte conexiones externas.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]