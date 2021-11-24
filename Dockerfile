# Dockerfile para despliegue automático de la aplicación CineTickets. Ejecución de tests
FROM python:3.8-alpine3.13

# Instalación de deps del gestor de tareas y deps, creación del usuario y descarga de script para instalar Poetry
RUN apk add \
    gcc \
    libc-dev \
    libffi-dev  \
    && addgroup -S cinetickets  \
    && adduser -S cinetickets -G cinetickets \
    && wget https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py

# Cambiar al usuario no root
USER cinetickets

# Cambio PATH para instalaciones en home de usuario no root
ENV PATH=/home/cinetickets/.local/bin:$PATH

# Instalación del gestor de dependencias y tareas
RUN python install-poetry.py \
    && pip install pypyr

# Cambiamos de directorio a /app/test
WORKDIR /app/test

# Ejecutamos los tests con el task runner
CMD ["pypyr", "tests"]
