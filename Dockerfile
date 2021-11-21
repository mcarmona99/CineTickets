# Dockerfile para despliegue automático de la aplicación CineTickes. Ejecución de tests
FROM python:3.6-alpine3.13

# Instalación del gestor de dependencias
RUN apk add gcc libc-dev libffi-dev && pip install poetry pypyr
