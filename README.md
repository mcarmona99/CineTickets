# CineTickets

## Descripción de la aplicación a desarrollar

La documentación referente al desarrollo de esta parte puede encontrarse en el directorio
[docs/hito_0](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_0).

En este directorio podemos encontrar un archivo `desarrollo_hito_0.md` que describe los pasos seguidos para la
realización del hito 0. A su vez, podemos encontrar un archivo `descripcion_problema.md` que incluye el desarrollo o MVP
del hito. En este caso se trata de la descripción de la aplicación a desarrollar.

## Concretando y planificando el proyecto

La documentación referente al desarrollo de esta parte puede encontrarse en el directorio
[docs/hito_1](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_1).

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

- [Interno 2 - Algoritmo básico de asignación de butacas en sala de cine](https://github.com/mcarmona99/CineTickets/milestone/3):
  este hito interno consiste en un producto mínimamente viable que incluye al anterior y que realiza la implementación
  de la función que corresponde con el algoritmo básico de asignación de butacas en una sala de cine. Usamos en este PMV
  el entorno de tests definido en el anterior hito para realizar los tests de la función implementada.

### Interno 1 - Preparación del entorno del proyecto

En este hito, como se ha mencionado anteriormente, se incluyen los gestores de tareas y dependencias y la biblioteca de
aserciones y marco de pruebas del proyecto.

Las siguientes issues pertenecen al hito:

#### [#22 - Se debe especificar un gestor de dependencias](https://github.com/mcarmona99/CineTickets/issues/22)

En esta tarea, se resuelve el problema referente a la especificación de un gestor de dependencias para el proyecto.

En la resolución de la issue, se estudian algunas alternativas y se decide utilizar el gestor de dependencias y paquetes
`Poetry`.

Se puede encontrar más información respectiva a la resolución de la tarea
en [docs/hito_2/gestor_dependencias.md](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_2/gestor_dependencias.md)
.

#### [#19 - Se necesita elegir un gestor de tareas](https://github.com/mcarmona99/CineTickets/issues/19)

En esta tarea, se resuelve el problema referente a la especificación de un gestor de tareas para el proyecto.

En la resolución de la issue, se decide utilizar el gestor de tareas `pypyr`. Esta elección se realiza tras consultar
ventajas y desventajas de algunas de las opciones que tenemos para gestores de tareas en
Python. [Esta lista](https://www.libhunt.com/t/task-runner) ha sido de utilidad. En ella encontramos un top de task
runners para proyecto open-source, que puede ser filtrado por lenguaje.

Analizo los siguientes tasks runner:

#### pypyr

Este task runner o gestor de tareas se usa para automatización y funciona con el lenguaje de marcas `yaml`. Como se
comenta en su [web oficial](https://pypyr.io/), este task runner se usa para cuando los scripts shell se vuelven algo
complejos. Más sencillo que un Makefile.

Con este gestor, se puede automatizar todo combinando comandos; y sobre todo y algo que lo hace muy versátil es que
podemos usar scripts escritos en distintos lenguajes de programación en un mismo pipeline.

Ejemplo: archivo `tests.yaml`

```yaml
# To execute this pipeline, shell something like:
# pypyr tests
steps:
  - name: pypyr.steps.cmd
    comment: Run the project tests using pytest.
    in:
      cmd: pytest
```

#### taskipy

Usado para tareas de pipeline de desarrollos, como pueden ser test, lint or publish.

Como ventaja, tiene la posibilidad de ser integrado con poetry, de forma que se puede añadir lo siguiente a poetry:

```toml
[tool.taskipy.tasks]
test = "python -m unittest tests/test_*.py"
lint = "pylint tests taskipy"
```

y también documentar cada task:

```toml
[tool.taskipy.tasks]
test = { cmd = "python -m unittest tests/test_*.py", help = "runs all unit tests" }
lint = { cmd = "pylint tests taskipy", help = "confirms code style using pylint" } 
```

para después lanzar cada task desde poetry con `poetry run task test`

Como desventaja, depende mucho de poetry, ya que su uso fuera de poetry está poco documentado. Otra desventaja es que
tasks con muchos commandos se pueden volver complejas, ya que estaríamos incluyéndolas en el `pyproject.toml` de poetry.

Fuertemente inspirado en el task runner de npm: [npm-run-script](https://docs.npmjs.com/cli/v8/commands/npm-run-script)

#### poethepoet

Muy similar a `taskipy`.

En este caso, tenemos completa dependencia de poetry.

```toml
[tool.poe.tasks]
  test       = "pytest --cov=poethepoet"                                # simple command based task
  mksandwich = { script = "my_package.sandwich:build" }                 # python script based task
  tunnel     = { shell = "ssh -N -L 0.0.0.0:8080:$PROD:8080 $PROD &" }  # shell script based task
```

En `poethepoet`, tenemos una de las ventajas de pypyr, podemos usar varios lenguajes y en este caso, especificar si es
lenguaje o apuntar a un script de otro directorio, ejemplo task `mksandwich`.

De nuevo como desventaja, complejidad si tenemos muchos comandos para una misma task.

#### invoke

Provee una API de alto nivel para lanzar comandos de shell.

Las tasks en invoke están escritas en python y agrupadas en forma de funciones en un archivo `tasks.py`, con lo que su
estructuración es limpia en cuanto a archivos. Se usa el decorador @task para indicar que una función representa una
tarea para el task runner.

Permite pasar parámetros a cada una de las tareas por medio de flags, lo que lo hace versátil:

```python
from invoke import task


@task
def clean(c, docs=False, bytecode=False, extra=''):
    patterns = ['build']
    if docs:
        patterns.append('docs/_build')
    if bytecode:
        patterns.append('**/*.pyc')
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        c.run("rm -rf {}".format(pattern))
```

Uso:

```bash
$ invoke clean --docs --bytecode build --docs --extra='**/*.pyo'
$ invoke clean -d -b build --docs -e '**/*.pyo'
$ invoke clean -db build -de '**/*.pyo'
```

#### Conclusión

Como conclusión, debato entre usar `pypyr` o `invoke`.

Descarto `taskipy` y `poethepoet` por su alta dependencia de `poetry` y porque al realizar tareas más complejas, se
pierde la facilidad de uso, ya que tendríamos que incorporar al `pyproject.toml` varias líneas para ejecución de una
misma tarea, lo que ensuciaría bastante el archivo.

Entre `pypyr` e `invoke`, decido usar `pypyr` por la modularización que propone. En este task runner, a diferencia
de `invoke`, podemos dividir cada tarea en un archivo distinto, lo que mejora la legibilidad de cada tarea a costa de
tener comandos y archivos distintos para cada tarea. Además de esto, tenemos la oportunidad de usar más lenguajes, cosa
que también aporta `invoke` pero con alguna limitación, ya que parte de un script de `python`.

Este task runner o gestor de tareas se usa para automatización y funciona con el lenguaje de marcas yaml. Como se
comenta en su web oficial, este task runner se usa para cuando los scripts shell se vuelven algo complejos.

Con este gestor, se puede automatizar todo combinando comandos; y sobre todo y algo que lo hace muy versátil es que
podemos usar scripts escritos en distintos lenguajes de programación en un mismo pipeline.

Siguiendo la guía encontrada en https://pypyr.io/docs/getting-started/run-your-first-pipeline/, creo
`my-first-pipeline.yaml` como archivo gestor de tareas base. Este primer pipeline se lanza de la siguiente forma:

```shell
$ pypyr my-first-pipeline
this is step 1
this is step 2
```

Este pipeline se ha adaptado para generar el archivo referente a la orden `installdeps` del proyecto:

```shell
$ pypyr installdeps
Installing dependencies from lock file

No dependencies to install or update
```

Se puede encontrar más información respectiva a la resolución de la tarea
en [docs/hito_2/gestor_tareas.md](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_2/gestor_tareas.md)
.

#### [#21 - Marco de pruebas](https://github.com/mcarmona99/CineTickets/issues/21)

Antes de mencionar las posibilidades de bibliotecas de aserciones y framework de tests, cabe destacar que se decide
llevar un desarrollo orientado a tests (TDD) frente a un desarrollo orientado a comportamiento (BDD), puesto que el
desarrollo mencionado se va a enfocar en el propio código y cómo debería de funcionar, en lugar de llevar un enfoque de
equipo y comportamiento del código. Se puede encontrar más información sobre las diferencias de TDD y BDD
en [esta web](https://www.itdo.com/blog/tdd-vs-bdd-expectativas-de-calidad-de-tus-desarrollos/.

De cara a la implementación del módulo de tests de la aplicación, se necesita elegir un marco de pruebas adecuado.

En esta issue, se deben de describir algunas de las alternativas propuestas y elegir la más adecuada.

Se estudian las siguientes alternativas: [robot](https://robotframework.org/)
, [pytest](https://docs.pytest.org/en/6.2.x/), [lettuce](https://github.com/gabrielfalcao/lettuce)
y [behave](https://behave.readthedocs.io/en/stable/)

#### lettuce

Marco de tests de tipo BDD, Behavior-driven-development, para python. Está inspirado en Cucumber de Ruby. Solo permite
realizar tests en Python, no deja mezclar lenguajes para el desarrollo de tests. Fue creado por la actual complejidad a
la hora de desarrollar tests unitarios de Python.

Ejemplo de uso de lettuce, para el siguiente escenario (códigos
de https://codefellows.github.io/sea-python-401d2/lectures/lettuce.html):

```
Feature: Simple FizzBuzz
    Implement a simple version of the FizzBuzz game

    Scenario: FizzBuzz of 5
        Given the number 5
        When I call FizzBuzz
        Then I see the output Buzz
```

Nos centramos en los pasos:

```
        When I call FizzBuzz
        Then I see the output Buzz
```

Usando lettuce, nuestros tests basados en BDD serían algo similar a lo siguiente. Archivo `steps.py`:

```python
@step('when I call fizzbuzz')
def call_fizzbuzz(step):
    world.fb = fizzbuzz(world.number)


@step('I see the output (\w+)')
def compare(step, expected):
    assert world.fb == expected, "Got %s" % expected
```

Al lanzar los tests, los tests pasan cuando las features, scenarios y steps se cumplen según los tests.

```
[fizzbuzz]
[master *=]
heffalump:fizzbuzz cewing$ lettuce
Feature: Simple FizzBuzz                          # features/fizzbuzz.feature:1
  Implement a simple version of the FizzBuzz game # features/fizzbuzz.feature:2
  Scenario: FizzBuzz of 5                         # features/fizzbuzz.feature:4
    Given the number 5                            # features/steps.py:8
    When I call FizzBuzz                          # features/steps.py:13
    Then I see the output Buzz                    # features/steps.py:18
    Traceback (most recent call last):
      ...
    AssertionError: Got None
1 feature (0 passed)
1 scenario (0 passed)
3 steps (1 failed, 2 passed)
```

### behave

De nuevo un marco de test de tipo BDD.

Permite que los tests estén escritos en lenguaje natural, con un bajo nivel en python, de la misma forma que se
desarrollaban con lettuce.

Podemos ver con el siguiente ejemplo, que es muy similar a lettuce (ejemplos
de https://behave.readthedocs.io/en/stable/tutorial.html):

Archivo `tutorial.feature`

```
Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!
```

Archivo `features/steps/tutorial.py`:

```
from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
```

### pytest

Marco de pruebas orientado a TDD.

Este marco de testing permite escribir test pequeños, pero que a su vez pueden aumentar en complejidad si decidimos
escalar a otros proyectos o librerías.

`pytest` sobrecarga el método assert de python para añadir información detallada en asserts que fallan. Además, `pytest`
puede autodescubrir módulos de tests y funciones usadas como tests. Permite el uso de decoradores de funciones
llamados `fixtures` que permiten parametrizar tests, realizar mocks, etc. Arquitectura que permite el uso de plugins
externos.

Ejemplo de uso de `pytest`:

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

### robot

Es un framework de automatización llamado por los desarrolladores como "genérico". Permite automatización de tests y
RPA (automatización de procesos robóticos). Tiene una sintaxis sencilla, con keywords descriptivas. Compatible con el
uso de otras librerías implementadas en python, java u otros lenguajes de programación.

Una ventaja de este framework frente a todos los demás, es que permite escribir tests de tipo BDD (orientados a
comportamiento), TDD (orientados a tests), DDD (orientados a datos), workflow tests, etc.

Ejemplos de uso de robot (https://github.com/robotframework/QuickStartGuide/blob/master/QuickStart.rst). Debido a su
estructura, permite ser usado como task runner y de hecho se recomienda cuando lo que se pretende automatizar no son
tests:

BDD:

```
*** Test Cases ***
User can change password
    Given a user has a valid account
    When she changes her password
    Then she can log in with the new password
    And she cannot use the old password anymore
```

DDD:

```
*** Test Cases ***
Invalid password
    [Template]    Creating user with invalid password should fail
    abCD5            ${PWD INVALID LENGTH}
    abCD567890123    ${PWD INVALID LENGTH}
    123DEFG          ${PWD INVALID CONTENT}
    abcd56789        ${PWD INVALID CONTENT}
    AbCdEfGh         ${PWD INVALID CONTENT}
    abCD56+          ${PWD INVALID CONTENT}
```

TDD:

```
*** Test Cases ***
Example
    Create Directory    ${TEMPDIR}/stuff
    Copy File    ${CURDIR}/file.txt    ${TEMPDIR}/stuff
    No Operation
```

```
*** Test Cases ***
Normal Error
    Fail    This is a rather boring example...

HTML Error
    ${number} =    Get Number
    Should Be Equal    ${number}    42    *HTML* Number is not my <b>MAGIC</b> number.
```

#### Conclusión

Como conclusión, descarto `lettuce` y `behave` ya que aunque son dos marcos de pruebas bastante poco complejos, busco un
framework test orientado a TDD lo cual hace que no me sirvan para el proyecto.

Entre `pytest` y `robot`, elijo `pytest` porque además de sus ventajas, es mucho más fácil de usar en comparación con
robot, que debido a su potente versatilidad pierde bastante en usabilidad.

#### [#20 - Biblioteca de aserciones](https://github.com/mcarmona99/CineTickets/issues/20)

Podemos usar numerosas bibliotecas de aserciones y marcos de tests en Python:

Bibliotecas de aserciones:

- grappa
- assertpy
- Verify

Marcos de tests:

- Robot
- Pytest
- Unittest
- DocTest
- Nose2
- Testify

Tras probar algunas de las bibliotecas de aserciones, se ha visto que `assertpy` es una biblioteca de aserciones con
funciones definidas con una sintaxis de "más alto nivel" y que por tanto hace que el desarrollo de tests sea más fácil.
La sintaxis de assertpy es muy similar a la vista en clase con los ejemplos mostrados (assert_that "algo", equal to "
otra cosa").

Con respecto al marco de tests, en el [repositorio de `assertpy`](https://github.com/assertpy/assertpy#usage) vemos que
recomiendan usar pytest, ya que es compatible con assertpy. Por esto, y por mi previa experiencia con pytest, lo elijo
como marco de tests.

Por tanto, el framework o marco de tests elegido es [pytest](https://pypi.org/project/pytest/). Este marco de testing
permite escribir test pequeños pero que a su vez pueden aumentar en complejidad si decidimos escalar a otros proyectos o
librerías.

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

Como biblioteca de aserciones, se puede usar la propia herramienta pytest, que ya contiene features o funciones tales
como pytest.raises, assert_called_with y otras funciones para mock, etc. Se usará pytest, pero también haremos uso de
assertpy, que es una biblioteca de aserciones con funciones definidas con una sintaxis de "más alto nivel" y que por
tanto hace que el desarrollo de tests sea más fácil.

Referencias de la biblioteca assertpy: [pypi](https://pypi.org/project/assertpy/)
y [GitHub](https://github.com/assertpy/assertpy)

```python
from assertpy import assert_that


def test_something():
    assert_that(1 + 2).is_equal_to(3)
    assert_that('foobar').is_length(6).starts_with('foo').ends_with('bar')
    assert_that(['a', 'b', 'c']).contains('a').does_not_contain('x')
```

### Interno 2 - Algoritmo básico de asignación de butacas en sala de cine

En este PMV, se desarrollan las issues siguientes:

- Se implementa un método de gestión de excepciones consideradas propias del
  proyecto: [Se necesita manejar excepciones propias del proyecto #29](https://github.com/mcarmona99/CineTickets/issues/29)

- Se implementan las funciones adecuadas relacionadas con la lógica de negocio referente a la asignación de butacas a
  una sala de cine, respetando
  restricciones: [Añadir entradas a una sala de cine sin redistribución de asientos #28](https://github.com/mcarmona99/CineTickets/issues/28)

A su vez, la historia de usuario
4: [HU4 - Empresa cinematográfica - Distribución de asientos en la venta de entradas](https://github.com/mcarmona99/CineTickets/issues/9)
se encuentra relacionada con este hito.

Se avanza en el proyecto en código y en tests.

Además de la resolución de estas dos issues, se incluye una tarea para lanzar los tests y otra para instalar
dependencias:

- `poetry run pypyr installdeps`
- `poetry run pypyr tests`
