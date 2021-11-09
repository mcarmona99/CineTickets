from cinetickets.CineTicketsException import CineTicketsException
from assertpy import *

def test_CineTicketsException():
    """Prueba que los objetos de la clase CineTicketsException son creados de manera satisfactoria."""
    # Arrange and Act
    CODIGO_TEST = 1
    ct_exception = CineTicketsException(CODIGO_TEST)

    # Assert
    assert_that(ct_exception).is_type_of(CineTicketsException)
    assert_that(ct_exception).is_instance_of(Exception)
    assert_that(ct_exception.codigo).is_equal_to(CODIGO_TEST)
    assert_that(ct_exception.mensaje).is_equal_to(CineTicketsException.ERROR_CODES_DESCRIPTION[CODIGO_TEST])

    # Arrange and Act
    CODIGO_TEST_NO_EXISTENTE = -99999
    ct_exception = CineTicketsException(CODIGO_TEST_NO_EXISTENTE)

    # Assert
    assert_that(ct_exception).is_type_of(CineTicketsException)
    assert_that(ct_exception).is_instance_of(Exception)
    assert_that(ct_exception.codigo).is_equal_to(CODIGO_TEST_NO_EXISTENTE)
    assert_that(ct_exception.mensaje).is_equal_to(CineTicketsException.MENSAJE_ERROR_NO_EXISTENTE)
