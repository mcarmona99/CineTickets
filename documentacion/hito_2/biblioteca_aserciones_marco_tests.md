# CineTickets

## Marco de tests

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

## Biblioteca de aserciones

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