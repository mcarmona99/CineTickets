# Dockerfile para despliegue automático de la aplicación CineTickets. Ejecución de tests
FROM python:3.8-alpine3.13

# Instalación del gestor de dependencias
RUN apk add gcc libc-dev libffi-dev && pip install poetry pypyr

COPY . /app

WORKDIR /app

RUN pypyr installdeps
CMD ["pypyr", "tests"]