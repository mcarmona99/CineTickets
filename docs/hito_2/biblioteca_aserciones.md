# CineTickets

Se estudian las siguientes alternativas: [assertpy](https://assertpy.github.io/docs.html)
, [grappa](https://pypi.org/project/grappa/)
, [verify](https://pypi.org/project/verify/)

#### grappa

Biblioteca de aserciones usada en python y permite crear tests a alto nivel para una mejor comprensión humana.

Incluye dos estilos de aserciones: `expect` y `should`, keywords que permiten orientar los tests de distintas formas.

Incluye también un reporte de errores detallado para tener un mejor feedback de los errores en tests y aportar agilidad
y mejor comprensión a los desarrolladores.

A continuación vemos ejemplos de tests escritos usando la librería `grappa`, tanto con `expect` como con `should` (
ejemplos de https://grappa.readthedocs.io/en/latest/style.html):

```
from grappa import should

foo = 'bar'
beverages = { 'tea': [ 'grappa', 'matcha', 'long' ] }

foo | should.be.a('string')
foo | should.equal('bar')
foo | should.have.length.of(3)
beverages | should.have.property('tea').with.length.of(3)

should(foo).be.a('string')
should('foo').to.be.equal('foo')
should('foo').have.length.of(3)
should(beverages).have.property('tea').with.length.of(3)
```

```
from grappa import expect

foo = 'bar'
beverages = { 'tea': [ 'grappa', 'matcha', 'long' ] }

foo | expect.to.be.a('string')
foo | expect.to.equal('bar')
foo | expect.to.have.length.of(3)
beverages | expect.to.have.property('tea').that.has.length.of(3)

expect(foo).to.be.a('string')
expect(foo).to.equal('bar')
expect(foo).to.have.length.of(3)
expect(beverages).to.have.property('tea').that.has.length.of(3)
```

Informes detallados de errores:

```
======================================================================
FAIL: tests.should_test.test_grappa_assert
======================================================================
Traceback (most recent call last):
File ".pyenv/versions/3.6.0/lib/python3.6/site-packages/nose/case.py", line 198, in runTest
self.test(*self.arg)
File "grappa/tests/should_test.py", line 16, in test_grappa_assert
x | should.be.have.length.of(4)
File "grappa/grappa/test.py", line 248, in __ror__
return self.__overload__(value)
File "grappa/grappa/test.py", line 236, in __overload__
return self.__call__(subject, overload=True)
File "grappa/grappa/test.py", line 108, in __call__
return self._trigger() if overload else Test(subject)
File "grappa/grappa/test.py", line 153, in _trigger
raise err
AssertionError: Oops! Something went wrong!

The following assertion was not satisfied
  subject "[1, 2, 3]" should be have length of "4"

Message
  subject list must have at least 4 items

Reasons
  ▸ unexpected object length: 3

What we expected
  an object that can be length measured and its length is equal to 4

What we got instead
  an object of type "list" with length 3

Information
  ▸ Object length is measured by using "len()" built-in
    Python function or consuming an lazy iterable, such as a
    generator. Most built-in types and objects in Python
    can be tested that way, such as str, list, tuple, dict...
    as well as any object that implements "__len__()" method.
    — Reference: https://docs.python.org/3/library/functions.html#len

Where
  File "grappa/tests/should_test.py", line 16, in test_grappa_assert

 8|
 9|  def test_native_assert():
10|      x = [1, 2, 3]
11|      assert len(x) == 4
12|
13|
14|  def test_grappa_assert():
15|      x = [1, 2, 3]
16| >    x | should.be.have.length.of(4)
17|
18|
19|  def test_bool():
20|      True | should.be.true | should.be.present
21|      False | should.be.false | should.be.equal.to(False)
22|      False | should.be.false | should.not_be.equal.to(True)
```

#### assertpy

`assertpy` es una biblioteca de aserciones que incluye funciones definidas con una sintaxis de "más alto nivel" y que
por tanto hace que el desarrollo de tests sea más fácil. La sintaxis de assertpy es muy similar a la vista en clase con
los ejemplos mostrados (`assert_that` "algo", `equal to` " otra cosa").

Ejemplo:

```python
from assertpy import assert_that


def test_something():
    assert_that(1 + 2).is_equal_to(3)
    assert_that('foobar').is_length(6).starts_with('foo').ends_with('bar')
    assert_that(['a', 'b', 'c']).contains('a').does_not_contain('x')
```

Como podemos ver, muy similar a grappa en lo que a sintaxis se refiere.

#### verify

De nuevo es una biblioteca de aserciones muy similar a las anteriores. Tiene una sintaxis de alto nivel y permite
keywords fáciles de entender para los desarrolladores.

Ejemplos de uso (de https://pypi.org/project/verify/):

```
from verify import expect, Not, Truthy, Falsy, Less, Greater

expect(5 * 5,
       Truthy(),
       Not(Falsy),
       Greater(15),
       Less(30))
```

También permite parametrizar funciones y usa AssertionError para manejo de excepciones:

```
def is_just_right(value):
    assert value == 'just right', 'Not just right!'

# Passes
expect('just right', is_just_right)

# Fails
try:
    expect('too cold', is_just_right)
except AssertionError:
    raise
```

#### Conclusion

A la hora de elegir entre estas tres bibliotecas de aserciones, no puedo tomar un criterio objetivo, ya que las tres son
muy similares y aportan funciones sencillas para la realización de los tests del proyecto.

Para elegir entre una de las tres, voy a los distintos proyectos de GitHub para ver cuál es la más usada (starred).
`assertpy` tiene 327 estrellas, `grappa` 123 y `verify` 62. Además de esto, `assertpy` es la más actualizada, con
commits incluidos en este mismo año.

Tras este breve análisis, elijo `assertpy` como biblioteca de aserciones.