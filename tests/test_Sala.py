from assertpy import *

from cinetickets.Sala import Sala


def test_Sala():
    """Prueba que los objetos de la clase Sala son creados de manera satisfactoria."""
    # Arrange
    id_sala, n_butacas_ancho, n_butacas_largo = 1, 2, 3

    # Act
    sala = Sala(id_sala=id_sala, n_butacas_ancho=n_butacas_ancho, n_butacas_largo=n_butacas_largo)

    # Assert
    assert_that(sala).is_type_of(Sala)
