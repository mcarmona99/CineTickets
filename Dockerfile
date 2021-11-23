# Dockerfile para despliegue automático de la aplicación CineTickets. Ejecución de tests
FROM python:3.8-alpine3.13

# Instalación del gestor de dependencias
RUN apk add gcc libc-dev libffi-dev && pip install poetry pypyr

# Cambiamos de directorio a /app/test
WORKDIR /app/test

# Ejecutamos los tests con el task runner
CMD ["pypyr", "tests"]
