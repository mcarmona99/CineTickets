# CineTickets

## Mejora de Dockerfile a partir de la primera iteración

Aplico cambios a la primera iteración del `Dockerfile`. Como referencia utilizo la documentación de `docker` para buenas
practicas en `Dockerfile`: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

En primer lugar, elimino `COPY . /app` del Dockerfile, ya que se usarán volúmenes (`-v` flag) para hacer el mapeo del
directorio.

A raíz de este cambio, y teniendo en cuenta que los tests se deben de lanzar con:

docker run -t -v `pwd`:/app/test nick-estudiante/nombre-del-repo

se cambiará el `WORKDIR` por `WORKDIR /app/test`, ya que `test` sera el directorio donde se encuentre el proyecto.

En segundo lugar, debemos de minimizar el número de capas. Esto sólo ocurre en versiones antiguas de Docker. Los
comandos que crean capas son `RUN`, `COPY` y `ADD`, entre otros. Otras instrucciones crean imágenes temporales
intermedias que no incrementan el tamaño de la construcción.

Para ello, mantengo la línea `RUN apk add gcc libc-dev libffi-dev` tal y como la tengo, en lugar de separar en
varios `RUN apk add x`.

Otra buena práctica, que en este caso es puramente de estilo, es ordenar los argumentos de comandos en más de una línea.
Para cumplir este check, cambio `RUN apk add gcc libc-dev libffi-dev` por

```
RUN apk add \
  gcc \
  libc-dev \
  libffi-dev
```

Finalmente, creo un usuario no root que será el que ejecute la aplicación. Este usuario ejecutará también las sentencias
pip install dentro del Dockerfile. Para cambiar a este usuario, uso `USER <usuario>`. Ejecutar pip con un usuario root
es una mala práctica ya que podríamos tener problemas de seguridad al descargar e instalar paquetes externos (de PyPI).
Ref: https://qastack.mx/ubuntu/802544/is-sudo-pip-install-still-a-broken-practice

Al crear un nuevo usuario, pypyr y poetry se instalan en el home del usuario: /home/cinetickets/.local/bin. También pasa
con otras dependencias:

```
  WARNING: The script normalizer is installed in '/home/cinetickets/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script doesitcache is installed in '/home/cinetickets/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script virtualenv is installed in '/home/cinetickets/.local/bin' which is not on PATH.
  ...
```

Usaremos ENV para actualizar la variable de entorno PATH que usa el software o paquetes instalados. Por ejemplo, como
vemos en la docu, `ENV PATH=/usr/local/nginx/bin:$PATH` se asegura que `CMD ["nginx"]` funciona. Para nuestro caso,
usaremos
`ENV PATH=/home/cinetickets/.local/bin:$PATH
`

Buenas prácticas en instrucciones de Dockerfile:

`FROM`: es recomendable usar Alpine. ✅
`RUN`: como hemos mencionado anteriormente, ordenar los argumentos de sentencias complejas de RUN en más de una línea. ✅
`CMD`: es recomendable usar los comandos separados por palabra (tipo string) en una lista.
Ex: `CMD ["executable", "param1", "param2"…]`. ✅
`USER`: si un servicio puede ser ejecutado sin privilegios, `USER` cambia a un usuario no root. Se deberá crear el
usuario y grupo en el Dockerfile. ✅

**Tras todos estos cambios, tanto de buenas prácticas como necesarios (como por ejemplo el usuario), nuestra imagen
tiene un tamaño de 224MB y queda de la siguiente forma:**

```Dockerfile
# Dockerfile para despliegue automático de la aplicación CineTickets. Ejecución de tests
FROM python:3.8-alpine3.13

# Instalación de deps del gestor de tareas y deps; y creación del usuario
RUN apk add \
    gcc \
    libc-dev \
    libffi-dev  \
    && addgroup -S cinetickets  \
    && adduser -S cinetickets -G cinetickets  # usuario y grupo, respectivamente

# Cambiar al usuario no root
USER cinetickets

# Cambio PATH para instalaciones en home de usuario no root
ENV PATH=/home/cinetickets/.local/bin:$PATH

# Instalación del gestor de dependencias y tareas
RUN pip install poetry pypyr

# Cambiamos de directorio a /app/test
WORKDIR /app/test

# Ejecutamos los tests con el task runner
CMD ["pypyr", "tests"]
```

Para construir la imagen:

```bash
$ docker build . -t mcarmona99/cinetickets
```

Para lanzar los tests (tengo que usar comillas ya que `pwd` tiene un path con espacios):

```
$ docker run -t -v "`pwd`:/app/test" mcarmona99/cinetickets

============================= test session starts ==============================
platform linux -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /app/test
collected 10 items                                                             

tests/test_Pelicula.py .....                                             [ 50%]
tests/test_Sala.py .                                                     [ 60%]
tests/test_exception.py ....                                             [100%]

=============================== warnings summary ===============================
../../home/cinetickets/.cache/pypoetry/virtualenvs/cinetickets-rAFghFJC-py3.8/lib/python3.8/site-packages/_pytest/cacheprovider.py:428
  /home/cinetickets/.cache/pypoetry/virtualenvs/cinetickets-rAFghFJC-py3.8/lib/python3.8/site-packages/_pytest/cacheprovider.py:428: PytestCacheWarning: cache could not write path /app/test/.pytest_cache/v/cache/nodeids
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../home/cinetickets/.cache/pypoetry/virtualenvs/cinetickets-rAFghFJC-py3.8/lib/python3.8/site-packages/_pytest/stepwise.py:49
  /home/cinetickets/.cache/pypoetry/virtualenvs/cinetickets-rAFghFJC-py3.8/lib/python3.8/site-packages/_pytest/stepwise.py:49: PytestCacheWarning: cache could not write path /app/test/.pytest_cache/v/cache/stepwise
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/warnings.html
======================== 10 passed, 2 warnings in 0.03s ========================
```

## Intentar optimizar instalaciónde dependencias del Dockerfile

En el Dockerfile, para instalar `poetry` y `pypyr`, previamente hacemos:

```
# Instalación de deps del gestor de tareas y deps; y creación del usuario
RUN apk add \
    gcc \
    libc-dev \
    libffi-dev  \
    && addgroup -S cinetickets  \
    && adduser -S cinetickets -G cinetickets  # usuario y grupo, respectivamente
```

Tenemos que buscar una alternativa a instalar las deps `gcc`, `libc-dev` y `libffi-dev`. Si evitamos instalar estas
dependencias, tendremos una construcción que resultará en una imagen más pequeña.

Empecemos con [Poetry](https://python-poetry.org/docs/).

Actualmente, instalamos Poetry con pip, con lo que bajamos la dependencia de el repo de Python PyPi. Como alternativa,
tal y como podemos encontrar en la [documentación de Poetry,](https://python-poetry.org/docs/#installation) podemos usar
un script escrito en Python para hacer esta instalación. El script se encuentra
en https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py.

En lugar de este script, probaremos con https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py.
Ambos son válidos, pero este último es más actual y será usado en futuras versiones.

`get-poetry` además, da errores con respecto a `gcc` aún teniéndolo instalado. Por esto, y por lo anteriormente
mencionado referente a actualizaciones, pruebo con `install-poetry`.

Tras hacer pruebas con install-poetry.py (la descarga del archivo la hacemos con wget, que es una dependencia ya
incluida en Alpine), veo que funciona con las actuales dependencias (gcc, libc-dev y libffi-dev), pero la construcción
no es válida cuando intento quitar al menos una de ellas:

```
...    
raise PoetryInstallationError(
__main__.PoetryInstallationError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "install-poetry.py", line 900, in <module>
    sys.exit(main())
  File "install-poetry.py", line 879, in main
    _, path = tempfile.mkstemp(
  File "/usr/local/lib/python3.8/tempfile.py", line 331, in mkstemp
    return _mkstemp_inner(dir, prefix, suffix, flags, output_type)
  File "/usr/local/lib/python3.8/tempfile.py", line 250, in _mkstemp_inner
    fd = _os.open(file, flags, 0o600)
PermissionError: [Errno 13] Permission denied: '/poetry-installer-error-misqhb2w.log'

```

Descarto entonces la instalación de `Poetry` por script ya que es inevitable instalar las tres dependencias mencionadas.
Aún con esto, cabe la posibilidad de instalar por script en lugar de usando `pip` (`PyPi`).

A priori, esta no es una buena alternativa ya que instalar mediante script aumenta considerablemente el tiempo de
construcción de la imagen. Aún así, instalar por script **es la mejor opción** o mejor dicho, **la recomendada** por sus
desarrolladores, ya que al instalar con otros métodos (`pip` o `pipx`) hacemos que Poetry siempre use la versión de
Python para la que fue instalado a la hora de crear nuevos entornos virtuales.

No tiene mucho sentido plantearnos ahora instalar `pypyr` por script, ya que, las dependencias `gcc`, `libc-dev`
y `libffi-dev` son instaladas siempre ya que son dependencias de `Poetry`. Aún así, investigo si esta instalación es
posible. Según su [documentación](https://github.com/pypyr/pypyr) oficial, no parece que existan scripts oficiales de
instalación, con lo que se hará usando `pip`.

**Con el uso del script para instalar poetry, el tamaño de la imagen construida es de 239MB.**
