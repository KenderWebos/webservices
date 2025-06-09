# Servicio de Transcripción de Audio

Este servicio web permite transcribir archivos de audio a texto utilizando Whisper, un modelo de reconocimiento de voz de OpenAI.

## Características

- Transcripción de audio a texto en español
- Interfaz web simple y fácil de usar
- Utiliza el modelo "small" de Whisper para un buen balance entre velocidad y precisión
- Contenedorizado con Docker para fácil despliegue

## Requisitos

- Docker
- Docker Compose (opcional)

## Instrucciones de uso

1. Construir la imagen:
```bash
docker build -t whisper-api .
```

2. Ejecutar el contenedor:
```bash
docker run -p 8000:8000 whisper-api
```

O alternativamente, usando Docker Compose:
```bash
docker-compose up
```

3. Abrir en el navegador:
```
http://localhost:8000
```

4. Subir un archivo de audio y hacer clic en "Transcribir"

## Estructura del Proyecto

```
whisper-transcriber/
├── Dockerfile
├── README.md
├── app/
│   └── main.py
└── docker-compose.yml
```

## Notas Técnicas

- El servicio está construido con FastAPI
- Utiliza Whisper para la transcripción de audio
- La interfaz web es simple y responsive
- El servicio está configurado para transcribir audio en español 