# Simple Dockerfile for backend (uses python:3.11-slim as base)
FROM python:3.11-slim
WORKDIR /app
COPY backend/requirements.txt ./
RUN apt-get update && apt-get install -y build-essential libsndfile1 ffmpeg git && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r backend/requirements.txt
COPY backend /app/backend
ENV PYTHONUNBUFFERED=1
EXPOSE 8080
CMD ["uvicorn","backend.app.main:app","--host","0.0.0.0","--port","8080","--lifespan","on"]
