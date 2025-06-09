FROM python:3.10-slim

RUN apt update && apt install -y ffmpeg && \
    pip install --no-cache-dir openai-whisper fastapi uvicorn

COPY app /app
WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 