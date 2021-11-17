# CineTickets

Antes de mencionar las posibilidades de bibliotecas de aserciones y framework de tests, cabe destacar que se decide
llevar un desarrollo orientado a tests (TDD) frente a un desarrollo orientado a comportamiento (BDD), puesto que el
desarrollo mencionado se va a enfocar en el propio código y cómo debería de funcionar, en lugar de llevar un enfoque de
equipo y comportamiento del código. Se puede encontrar más información sobre las diferencias de TDD y BDD
en [esta web](https://www.itdo.com/blog/tdd-vs-bdd-expectativas-de-calidad-de-tus-desarrollos/.

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

#### behave

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

#### pytest

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

#### robot

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
