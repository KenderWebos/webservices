# Servicios Web

Este repositorio contiene una colección de servicios web útiles, cada uno contenedorizado con Docker para fácil despliegue y uso.

## Estructura del Repositorio

```
.
├── services/
│   ├── whisper-transcriber/    # Servicio de transcripción de audio a texto
│   └── [otros-servicios]/      # Futuros servicios
└── README.md
```

## Servicios Disponibles

### 1. Whisper Transcriber
Un servicio web que permite transcribir archivos de audio a texto utilizando Whisper.

[Ver detalles del servicio](services/whisper-transcriber/README.md)

## Servicios Planificados

### 1. Servicio de Compresión de Imágenes
- Compresión de imágenes manteniendo calidad aceptable
- Soporte para múltiples formatos (JPG, PNG, WebP)
- API REST para procesamiento por lotes
- Interfaz web para subir y procesar imágenes

### 2. Servicio de Conversión de Documentos
- Conversión entre formatos de documentos (PDF, DOCX, TXT)
- Extracción de texto de PDFs
- OCR para documentos escaneados
- API REST y webhook para integración

### 3. Servicio de Análisis de Sentimiento
- Análisis de sentimiento de texto en español
- Clasificación de emociones
- API REST para análisis en tiempo real
- Interfaz web para análisis de textos largos

### 4. Servicio de Generación de Resúmenes
- Generación automática de resúmenes de texto
- Extracción de palabras clave
- Soporte para múltiples idiomas
- API REST para integración con otros servicios

### 5. Servicio de Traducción
- Traducción entre múltiples idiomas
- Detección automática de idioma
- API REST para traducción en tiempo real
- Interfaz web para traducción de documentos

## Cómo Contribuir

1. Cada nuevo servicio debe estar en su propia carpeta dentro del directorio `services/`
2. Cada servicio debe incluir:
   - Un README.md con documentación completa
   - Un Dockerfile para contenerización
   - Un docker-compose.yml (opcional)
   - Cualquier otro archivo necesario para el funcionamiento del servicio

## Requisitos Generales

- Docker
- Docker Compose (opcional, dependiendo del servicio)

## Licencia

Este proyecto está bajo la Licencia MIT.
