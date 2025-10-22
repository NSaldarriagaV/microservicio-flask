# Imagen base de Python
FROM python:3.12-slim

# Previene buffering de logs
ENV PYTHONUNBUFFERED=1

# Crea usuario no root por seguridad (opcional)
RUN useradd -ms /bin/bash appuser

# Instala dependencias del sistema (si fueran necesarias)
RUN apt-get update && apt-get install -y --no-install-recommends     ca-certificates  && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Copia requirements primero para aprovechar capas de cache
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código
COPY app.py /app/app.py

# Cambia propietario
RUN chown -R appuser:appuser /app
USER appuser

# Exponer puerto
EXPOSE 8000

# Comando por defecto (producción)
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "app:app"]
