# CineTickets

## Se debe especificar un gestor de dependencias

Se debe especificar un gestor de dependencias adecuado para la aplicación.

En esta issue, se deben de describir algunas de las alternativas propuestas y elegir la más adecuada.

### Alternativa 1 - `pip`

`pip` es el sistema de gestión de paquetes o dependencias para instalar y administrar librerías en Python. Este gestor
nos ayuda a tener las librerías externas que usamos en el proyecto organizadas.

Viene instalado por defecto en muchas versiones de **Python2** y **Python3**.

#### Ventajas

Capacidad de instalar varias dependencias con un único comando, haciendo uso de un archivo `requirements.txt`.

`pip3 install -r requirements.txt
`

#### Desventajas

Al desarrollar, es posible que se esté trabajando en más de un proyecto al mismo tiempo. Esto da lugar a que se
necesiten cambios de versiones de dependencias y/o frameworks. Esto puede ocurrir también dentro del mismo proyecto, si
estamos trabajando en issues de distintas versiones del mismo. Por ejemplo, si trabajamos en `CineTickets`, podríamos
estar arreglando un bug para 3.1 y luego cambiar a 3.2 para añadir una feature, eso quizás necesitase de un cambio de
versiones de dependencias. Una desventaja de `pip` es que no podemos cambiar de dependencias fácilmente si no usamos
herramientas o librerías externas como `virtualenv`.

### Alternativa 2 - `poetry`

`Poetry` es una herramienta para gestionar dependencias y paquetes en **Python**. `Poetry` permite declarar las
librerías de las que depende el proyecto y las gestionará (instalaciones, actualizaciones, etc.)

`Poetry` requiere **Python** con version 2.7 o una version mayor o igual a 3.5.

Esta herramienta usa internamente `pip` para instalar paquetes.

#### Ventajas

Mejor resolutor de dependencias (dependency resolver) que en `pip`, en términos de estabilidad.

Capaz de gestionar dependencias de producción y de desarrollo de forma separada: versiones específicas de un paquete,
etc. (Principal desventaja de pip y que sí es posible en `Poetry`).

#### Desventajas

Ligeramente más lento que `pip`.

## Conclusión

Debido a las ventajas que tiene sobre `pip`, se elige `poetry` como gestor de dependencias del proyecto. La desventaja
de `poetry` es el rendimiento frente a `pip`, como hemos dicho, pero se considerará asumir este riesgo para conseguir la
estabilidad mencionada de cara a gestionar dependencias.

En el PR relativo a esta issue se añadirá información relativa a la instalación y configuración de poetry e información
adicional.