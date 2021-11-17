from datetime import datetime

import pytest
from assertpy import *

from cinetickets.Pelicula import Pelicula, PeliculaFecha
from cinetickets.Sala import Sala


def test_Pelicula():
    """Prueba que los objetos de la clase Pelicula son creados de manera satisfactoria."""
    # Arrange
    nombre, fecha_lanzamiento, genero = 'test', datetime(2021, 1, 1), 'test_genero'

    # Act
    p = Pelicula(nombre=nombre, fecha_lanzamiento=fecha_lanzamiento, genero=genero)

    # Assert
    assert_that(p).is_type_of(Pelicula)


def test_PeliculaFecha():
    """Prueba que los objetos de la clase PeliculaFecha son creados de manera satisfactoria."""
    # Arrange
    nombre, fecha_lanzamiento, genero = 'test', datetime(2021, 1, 1), 'test_genero'
    fecha_proyeccion = datetime(2021, 1, 1, 21, 30, 00)
    id_sala, n_butacas_ancho, n_butacas_largo = 1, 2, 3
    sala = Sala(id_sala=id_sala, n_butacas_ancho=n_butacas_ancho, n_butacas_largo=n_butacas_largo)

    # Act
    p = PeliculaFecha(nombre=nombre,
                      fecha_lanzamiento=fecha_lanzamiento,
                      genero=genero,
                      fecha_proyeccion=fecha_proyeccion,
                      sala_proyeccion=sala)

    # Assert
    assert_that(p).is_instance_of(Pelicula)
    assert_that(p).is_type_of(PeliculaFecha)
    assert_that(p.distribucion).is_equal_to([[0, 0], [0, 0], [0, 0]])


@pytest.mark.parametrize('distribucion, distribucion_esperada, tamano_nuevo_grupo', [
    (
            [['1', '0', '1'], ['0', '0', '0'], ['2', '0', '2']],
            [['1', '0', '1'], ['0', '3', '0'], ['2', '0', '2']],
            1
    ),
    (
            [['1', '0', '1'], ['0', '0', '0'], ['2', '0', '2']],
            [['1', '0', '1'], ['0', '0', '0'], ['2', '0', '2']],
            2
    ),
    (
            [['1', '0', '0', '1'], ['0', '0', '0', '0'], ['2', '0', '0', '2']],
            [['1', '0', '0', '1'], ['0', '3', '3', '0'], ['2', '0', '0', '2']],
            2
    ),
])
def test_anadir_grupo_a_distribucion(distribucion, distribucion_esperada, tamano_nuevo_grupo):
    """Prueba la funcion anadir_grupo_a_distribucion de la clase PeliculaFecha."""
    # Arrange
    nombre, fecha_lanzamiento, genero = 'test', datetime(2021, 1, 1), 'test_genero'
    fecha_proyeccion = datetime(2021, 1, 1, 21, 30, 00)
    id_sala, n_butacas_ancho, n_butacas_largo = 1, 2, 3
    sala = Sala(id_sala=id_sala, n_butacas_ancho=n_butacas_ancho, n_butacas_largo=n_butacas_largo)
    p = PeliculaFecha(nombre=nombre, fecha_lanzamiento=fecha_lanzamiento, genero=genero,
                      fecha_proyeccion=fecha_proyeccion, sala_proyeccion=sala, distribucion=distribucion)

    # Act
    p.anadir_grupo_a_distribucion(tamano_nuevo_grupo=tamano_nuevo_grupo)

    # Assert
    assert_that(p.distribucion).is_equal_to(distribucion_esperada)
