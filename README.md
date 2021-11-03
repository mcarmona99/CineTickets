# CineTickets

## Descripción de la aplicación a desarrollar

La documentación referente al desarrollo de esta parte puede encontrarse en el directorio
[documentacion/hito_0](https://github.com/mcarmona99/CineTickets/blob/master/documentacion/hito_0).

En este directorio podemos encontrar un archivo `desarrollo_hito_0.md` que describe los pasos seguidos para la
realización del hito 0. A su vez, podemos encontrar un archivo `descripcion_problema.md` que incluye el desarrollo o MVP
del hito. En este caso se trata de la descripción de la aplicación a desarrollar.

## Concretando y planificando el proyecto

La documentación referente al desarrollo de esta parte puede encontrarse en el directorio
[documentacion/hito_1](https://github.com/mcarmona99/CineTickets/blob/master/documentacion/hito_1).

En este directorio podemos encontrar un archivo `planificacion.md` que describe los pasos seguidos para realizar la
primera de planificación del proyecto, donde concretamos hitos e historias de usuario.

## Infraestructura y tests del proyecto

En este apartado añadimos tests y una descripción inicial del entorno o infraestructura de la aplicación, donde se
concretan los gestores de dependencias y tareas. Para la adición de tests, se necesita una biblioteca de aserciones y
marco de pruebas, ambos añadidos también en este apartado.

En primer lugar, cabe mencionar que esta parte del proyecto se divide en la entrega de dos productos mínimamente viables
o hitos; en este caso internos:

- [Interno 1 - Preparación del entorno del proyecto](https://github.com/mcarmona99/CineTickets/milestone/6): en este
  hito interno, se avanza con respecto al hito anterior y se incluyen los gestores de tareas y dependencias y la
  biblioteca de aserciones y marco de pruebas.

- [Interno 2 - Algoritmo básico de redistribución de butacas en sala de cine](https://github.com/mcarmona99/CineTickets/milestone/3):
  este hito interno consiste en un producto mínimamente viable que incluye al anterior y que realiza la implementación
  de la función que corresponde con el algoritmo básico de redistribución de butacas en una sala de cine. Usamos en este
  PMV el entorno de tests definido en el anterior hito para realizar los tests de la función implementada.

### Interno 1 - Preparación del entorno del proyecto

En este hito, como se ha mencionado anteriormente, se incluyen los gestores de tareas y dependencias y la biblioteca de
aserciones y marco de pruebas del proyecto.

Las siguientes issues pertenecen al hito:

#### [#22 - Se debe especificar un gestor de dependencias](https://github.com/mcarmona99/CineTickets/issues/22)

En esta tarea, se resuelve el problema referente a la especificación de un gestor de dependencias para el proyecto.

En la resolución de la issue, se estudian algunas alternativas y se decide utilizar el gestor de dependencias y paquetes
`Poetry`.

Se puede encontrar más información respectiva a la resolución de la tarea
en [documentacion/hito_2/gestor_dependencias.md](https://github.com/mcarmona99/CineTickets/blob/master/documentacion/hito_2/gestor_dependencias.md)
.

#### [#19 - Se necesita elegir un gestor de tareas](https://github.com/mcarmona99/CineTickets/issues/19)

En esta tarea, se resuelve el problema referente a la especificación de un gestor de tareas para el proyecto.

En la resolución de la issue, se decide utilizar el gestor de tareas `pypyr`.

Siguiendo la guía encontrada en https://pypyr.io/docs/getting-started/run-your-first-pipeline/, creo
`my-first-pipeline.yaml` como archivo gestor de tareas base. Este primer pipeline se lanzaría con `poetry`, como se ha
especificado en la issue anterior:

```shell
$ poetry run pypyr my-first-pipeline
this is step 1
this is step 2
```

Este pipeline se ha adaptado para generar el archivo referente a la orden `installdeps` del proyecto:

```shell
$ poetry run pypyr installdeps
Installing dependencies from lock file

No dependencies to install or update
```

Se puede encontrar más información respectiva a la resolución de la tarea
en [documentacion/hito_2/gestor_tareas.md](https://github.com/mcarmona99/CineTickets/blob/master/documentacion/hito_2/gestor_tareas.md)
.

#### [#20 - Biblioteca de aserciones](https://github.com/mcarmona99/CineTickets/issues/20) y [#21 - Marco de pruebas](https://github.com/mcarmona99/CineTickets/issues/21)

El framework o marco de tests elegido es [pytest](https://pypi.org/project/pytest/). Este marco de testing permite escribir test pequeños pero que a su vez pueden aumentar en complejidad si decidimos escalar a otros proyectos o librerías.

Ejemplo de uso de pytest:

```python
# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
```

```bash
$ pytest
============================= test session starts =============================
collected 1 items

test_sample.py F

================================== FAILURES ===================================
_________________________________ test_answer _________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_sample.py:5: AssertionError
========================== 1 failed in 0.04 seconds ===========================
```

Como biblioteca de aserciones, se puede usar la propia herramienta pytest, que ya contiene features o funciones tales como pytest.raises, assert_called_with y otras funciones para mock, etc.
Se usará pytest, pero también haremos uso de assertpy, que es una biblioteca de aserciones con funciones definidas con una sintaxis de "más alto nivel" y que por tanto hace que el desarrollo de tests sea más fácil.

Referencias de la biblioteca assertpy: [pypi](https://pypi.org/project/assertpy/) y [GitHub](https://github.com/assertpy/assertpy)

```python
from assertpy import assert_that

def test_something():
    assert_that(1 + 2).is_equal_to(3)
    assert_that('foobar').is_length(6).starts_with('foo').ends_with('bar')
    assert_that(['a', 'b', 'c']).contains('a').does_not_contain('x')
```