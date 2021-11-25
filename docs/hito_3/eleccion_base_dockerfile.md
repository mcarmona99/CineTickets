# CineTickets

## Elección de base

Se añade un archivo `Dockerfile` al directorio principal del proyecto.

El Dockerfile contendrá las órdenes necesarias para construir el contenedor. Para su construcción, ejecutaremos

`docker build .`

Comenzamos con la imagen base del contenedor. Como primera imagen a utilizar, usamos `ubuntu` (
Ref.: https://hub.docker.com/_/ubuntu). Se puede especificar versión, si no ponemos ninguna, con

`FROM ubuntu`

construiremos un contenedor con la última versión estable de `ubuntu` (`ubuntu:latest`).

Con la última versión (`ubuntu:latest`), tenemos una imagen de **72.8MB**.

Como la versión actualmente no es un problema ni un requisito para la aplicación, probamos a usar distribuciones
antiguas de ubuntu. Por ejemplo si usamos 18.04, la imagen tiene un peso de **63,1 MB**. Para ello
usamos `FROM ubuntu:18.04`.

Vemos que el peso de la imagen ha disminuido. Probamos entonces con distribuciones menos pesadas, para optimizar el
tamaño del contenedor.

[alpine](https://hub.docker.com/_/alpine):

Alpine es conocido por ser una distribución de Linux ligera y ser el SO base más ligero para usar en contenedores
docker. En su web tenemos la descripción:

> A minimal Docker image based on Alpine Linux with a complete package index and only 5 MB in size!

Tras probarlo en nuestro Dockerfile vemos que su imagen pesa 5.61MB.

De nuevo podemos ver si disminuimos esto con [versiones anteriores](https://hub.docker.com/_/alpine/?tab=tags) de
Alpine, ya que la última usada es la latest. Actualmente, la última versión disponible es la 3.14.

Con la versión 3.12 de Alpine, tenemos una imagen base de 5.59MB. Con la versión 3.11 de Alpine, tenemos una imagen base
de 5.62MB. ... Con la versión 3.6 de Alpine, tenemos una imagen base de 4.03MB. ... Con la versión 3.1 de Alpine,
tenemos una imagen base de 4.5MB. ... Con la versión 2.6 de Alpine, que es la más antigua disponible, tenemos una imagen
base de 4.5MB.

En lugar de probar versiones y ver cada tamaño por separado, podemos ver el compressed size de cada uno de los tags en
la link anterior, que muestra los tags de Alpine. Podemos ver que la imagen 3.5 de Alpine es la que tiene menor
compressed size, para todas las distribuciones, que es de 1.88 MB. Probando esta versión en el Dockerfile, tenemos una
imagen base de 4MB.

NOTA: otra posibilidad vista en clase es la de
usar [docker diff](https://docs.docker.com/engine/reference/commandline/diff/). Este comando permite ver las diferencias
entre imágenes locales o remota. Muestra diferencias a nivel de archivos y paquetes instalados en cada imagen.

Tras este análisis, **nos quedamos con alpine:3.5 como imagen base del contenedor.**

### Otra alternativa

A continuación, debemos de instalar los paquetes adicionales necesarios (actualmente ninguno) así como el task runner y
dependencias del mismo.

Previo al task runner, tenemos que instalar el gestor de dependencias. El gestor de dependencias que usamos es `poetry`
. `Poetry` necesita ser instalado desde `pip` por lo que necesitamos `python` y `pip` como dependencias.

El siguiente paso por tanto es descargar estas dependencias.

Para instalar dependencias en `Alpine`, tenemos que usar `apk add dependencia`. Para hacer esto dentro del `Dockerfile`,
usamos el comando `RUN`, que lanza comandos en tiempo de construcción del contenedor.

Para el ejemplo de `python3`,

```
RUN apk add python3

devolverá el siguiente error:

Step 2/2 : RUN apk add python3
 ---> Running in 8c2ae831e9ff
WARNING: Ignoring APKINDEX.c51f8f92.tar.gz: No such file or directory
WARNING: Ignoring APKINDEX.d09172fd.tar.gz: No such file or directory
ERROR: unsatisfiable constraints:
  python3 (missing):
    required by: world[python3]
The command '/bin/sh -c apk add python3' returned a non-zero code: 1
```

Este error ocurre porque estamos usando una distribución antigua de `Alpine` y probablemente no esté `python3` en el
repositorio. Usamos entonces `apk add --update --no-cache python3` y de este modo instalaremos la dependencia
correctamente.

Tras esto, el `Dockerfile` contiene:

```
# Dockerfile para despliegue automático de la aplicación CineTickes. Ejeción de tests
FROM alpine:3.5

RUN apk add --update --no-cache python3
```

y su peso tras construir la imagen es de `60.7MB`.

La versión de `Python` no nos interesa ya que sólo lo queremos para instalar `Poetry`. Podemos entonces
instalar `python2` en lugar de `python3` y de esta forma disminuir un poco el tamaño de la imagen.
Con `RUN apk add --update --no-cache python`, tenemos una imagen de `44.2MB`.

El peso ha aumentado considerablemente con respecto a la imagen inicial de `Alpine`. Para evitar esta subida, podemos
proponernos usar una distribución base que ya contenga python instalado. Como es lógico, buscamos una
distribución `Alpine` con `Python`.

En la web de Docker Hub, imagen oficial de Python: https://hub.docker.com/_/python?tab=description, tenemos imágenes
para todas las versiones de `Python` y distribuciones. Tomamos entonces la más ligera y que use `Alpine`.

Usando `FROM python:alpine`, tenemos las últimas versiones de ambos y conseguimos un tamaño de `45.5 MB`. Si estudiamos
versiones para intentar tener tamaños más pequeños de imagen, podemos tomar las dos más pequeñas disponibles tanto de
python como de Alpine, 3.6 y 3.13, respectivamente.

Con las versiones mencionadas, tenemos una imagen de `40.8MB`, imagen incluso más pequeña que la que conseguimos con
Alpine y luego instalando python2.

Como última base a estudiar, tenemos `python:slim` (y sus respectivas imagenes si especificamos versiones). Esta imagen
es una imagen basada en ubuntu con python instaldo que no contiene los paquetes comunes contenidos en los tags por
defecto de python. Por tanto, esta imagen contiene paquetes mínimos para ejecutar python. Esta imagen es más pesada que
Alpine, 122MB, por lo que la descartamos.

**Tras este análisis, me quedo con la imagen base python:3.6-alpine3.13, con la que hemos conseguido un tamaño de
40.8MB.**

Volviendo al principal objetivo del anterior comentario, debemos de instalar los paquetes adicionales necesarios (
actualmente ninguno) así como el task runner y dependencias del mismo.

Empezamos instalando `poetry`, que viene a ser nuestro gestor de dependencias. Si hacemos `RUN pip install poetry`, nos
encontramos con el siguiente error:

```
...
    unable to execute 'gcc': No such file or directory
    error: command 'gcc' failed with exit status 1
```

Parece ser que nos falta el compilador de gcc. Procedemos a instalarlo.

Tras evitar ese error instalando gcc, tenemos uno nuevo relacionado con la librería limits.h, output:

usr/local/include/python3.6m/Python.h:11:10: fatal error: limits.h: No such file or directory

Solucionamos este error instalando libc-dev. Tras esto, veo más errores. Voy instalando las dependencias necesarias
hasta que consigamos instalar poetry.

Finalmente, tenemos el siguiente `Dockerfile`:

```
# Dockerfile para despliegue automático de la aplicación CineTickes. Ejecución de tests
FROM python:3.6-alpine3.13

RUN apk add gcc libc-dev libffi-dev && pip install poetry
```

En total, la imagen supone un tamaño de 225MB.

Una vez que tenemos el gestor de dependencias, instalamos el task runner, que es `pypyr`. No necesitamos dependencias ya
que las dependencias son las mismas que las que instalamos para poetry. El tamaño aumenta a **229MB**.

A continuación, tenemos que realizar los pasos para instalar dependencias con el task runner y lanzar los tests.

En primer lugar, copiamos a /app todo el proyecto y cambiamos desde el dockerfile a /app:

COPY . /app

WORKDIR /app

Después, ejecutamos la task de installdeps:

CMD ["pypyr", "installdeps"]

El primer error que encontramos es el siguiente:

```
The currently activated Python version 3.6.15 is not supported by the project (^3.8).
Trying to find and use a compatible version. 

  NoCompatiblePythonVersionFound

...

CalledProcessError: Command '['poetry', 'install']' returned non-zero exit status 1.
```

Este error se debe a que en el pyproject.toml de poetry, se especificó que la versión de python necesaria para el
proyecto tenía que ser igual o superior a 3.8. Esto es algo que no he tenido en cuenta cuando elegimos el sistema
operativo base, que finalmente fue Alpine 3.13 con python 3.6 por ser ligero. Tomamos entonces Alpine de nuevo 3.13 pero
con version de python3.8. Este cambio no debe suponer una diferencia muy grande en cuanto a tamaño de la imagen.

Tras el cambio comentado, la imagen pasa de pesar 229 MB a pesar 231MB, lo cual no supone ningún problema.

Finalmente, lanzamos los tests con el gestor de tareas. El `Dockerfile` queda de la siguiente forma y la imagen
resultado tiene un tamaño de **257MB**.

```
# Dockerfile para despliegue automático de la aplicación CineTickets. Ejecución de tests
FROM python:3.8-alpine3.13

# Instalación del gestor de dependencias
RUN apk add gcc libc-dev libffi-dev && pip install poetry pypyr

COPY . /app

WORKDIR /app

RUN pypyr installdeps
CMD ["pypyr", "tests"]
```

Output:

```bash
$ docker run -t 28e4ea17f891
============================= test session starts ==============================
platform linux -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /app
collected 10 items                                                             

tests/test_Pelicula.py .....                                             [ 50%]
tests/test_Sala.py .                                                     [ 60%]
tests/test_exception.py ....                                             [100%]

============================== 10 passed in 0.04s ==============================

```

Para optimizar el `Dockerfile` anteriormente definido, he añadido el step de instalar dependencias al
pipeline `tests.yaml`. De esta forma, cuando hacemos `pypyr tests`, automáticamente instalamos las dependencias
necesarias (`pytest` y `assertpy`).

Con este cambio, nos ahorramos el paso `RUN pypyr installdeps`, ya que va implícito en `CMD ["pypyr", "tests"]`. Esto
supone una mejora en tamaño, con lo que disminuimos a **231MB**.

ESTE PASO NO ES VÁLIDO, ISSUE ABIERTA Y QUE LO RESUELVE: [#49](https://github.com/mcarmona99/CineTickets/issues/49).

COMENTARIO SOBRE DICHA RESOLUCIÓN Y DECISIÓN FINAL:

Elimino la llamada a la task installdeps de tests.

En la construcción del contenedor, las dependencias del proyecto ya deben de quedar instaladas, y no deben de instalarse
por tanto en tiempo de ejecución (CMD).

Para esto, se necesita añadir una nueva capa en el Dockerfile con la instrucción `COPY`, que copie el pipeline
de `installdeps` y el `pyproject.toml`.

Además, también tenemos que añadir una nueva capa de `RUN`, ya que, la instalación de dependencias tiene que ser
en `/app/test` o de lo contrario, tendremos un error al lanzar los tests diciendo que no encuentra `pytest`:

```
[Errno 2] No such file or directory: b'/bin/pytest' 
```

Archivo final:

```
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

# Copia pipeline de instalar dependencias y archivos de poetry e instala dependencias
COPY installdeps.yaml pyproject.toml poetry.lock ./
RUN pypyr installdeps

# Ejecutamos los tests con el task runner
CMD ["pypyr", "tests"]
```

Tras investigar veo otra alternativa. Podemos reducir una capa si nos llevamos WORKDIR arriba del todo y de esa forma,
descargamos el script de Poetry en /app/test. Ahorramos así el RUN pypyr installdeps ya que lo podríamos hacer justo
después de la instalación de pypyr. Para esto, también hay que llevarse COPY antes de las instalaciones de poetry y
pypyr.

Dockerfile final, con un peso de **264MB**. La subida de tamaño es normal ya que hemos añadido dependencias del proyecto
a la fase de construcción:

```
# Dockerfile para despliegue automático de la aplicación CineTickets. Ejecución de tests
FROM python:3.8-alpine3.13

# Cambiamos de directorio a /app/test
WORKDIR /app/test

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

# Copia pipeline de instalar dependencias y archivos de poetry e instala dependencias
COPY installdeps.yaml pyproject.toml poetry.lock ./

# Instalación del gestor de dependencias y tareas; e instalación de deps del proyecto
RUN python install-poetry.py \
    && pip install pypyr \
    && pypyr installdeps

# Ejecutamos los tests con el task runner
CMD ["pypyr", "tests"]
```
