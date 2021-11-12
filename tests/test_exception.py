import pytest
from assertpy import *

from cinetickets.exception import CineTicketsClientError, CineTicketsServerError, CineTicketsNotFound


def test_CineTicketsClientError():
    """Prueba que los objetos de la clase CineTicketsClientError son creados de manera satisfactoria."""
    # Arrange
    msg = 'Ejemplo'

    # Act
    ct_exception = CineTicketsClientError(msg)

    # Assert
    assert_that(ct_exception).is_type_of(CineTicketsClientError)
    assert_that(ct_exception).is_instance_of(Exception)
    assert_that(ct_exception.args[0]).is_equal_to(f'CLIENT ERROR: {msg}')


def test_CineTicketsServerError():
    """Prueba que los objetos de la clase CineTicketsServerError son creados de manera satisfactoria."""
    # Arrange
    msg = 'Ejemplo'

    # Act
    ct_exception = CineTicketsServerError(msg)

    # Assert
    assert_that(ct_exception).is_type_of(CineTicketsServerError)
    assert_that(ct_exception).is_instance_of(Exception)
    assert_that(ct_exception.args[0]).is_equal_to(f'SERVER ERROR: {msg}')


class RecursoDummy:
    def __init__(self):
        self.var1 = 'variable1'
        self.var2 = 'variable2'


@pytest.mark.parametrize('argumento', [RecursoDummy(), 'Ejemplo'])
def test_CineTicketsNotFound(argumento):
    """Prueba que los objetos de la clase CineTicketsNotFound son creados de manera satisfactoria."""
    # Act
    ct_exception = CineTicketsNotFound(argumento)

    # Assert
    assert_that(ct_exception).is_type_of(CineTicketsNotFound)
    assert_that(ct_exception).is_instance_of(CineTicketsClientError)
    assert_that(ct_exception.args[0]).is_equal_to(
        f'CLIENT ERROR: Recurso no encontrado: '
        f'{argumento if isinstance(argumento, str) else f"{type(argumento)} con atributos {argumento.__dict__}"}')
