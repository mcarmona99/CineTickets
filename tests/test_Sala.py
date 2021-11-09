import pytest
from assertpy import *

from exceptions.CineTicketsException import CineTicketsException
from models.Pelicula import PeliculaFecha
from models.Sala import Sala


def test_Sala():
    """Prueba que los objetos de la clase Sala son creados de manera satisfactoria."""
    # Arrange
    distribucion = {'pelicula_test': [['1', '1'], ['0', '0'], ['2', '2']]}

    # Act
    sala = Sala(id_sala=1, n_butacas_ancho=2, n_butacas_largo=3,
                distribucion_por_pelicula=distribucion)

    # Assert
    assert_that(sala).is_type_of(Sala)


def test_obtener_distribucion_por_pelicula():
    """Prueba la funcion obtener_distribucion_por_pelicula de la clase Sala."""
    # Arrange
    nombre_pelicula = 'pelicula_test'
    nombre_pelicula_no_existente = 'pelicula_test_no_existente'
    distribucion = {nombre_pelicula: [['1', '1'], ['0', '0'], ['2', '2']]}
    sala = Sala(id_sala=1, n_butacas_ancho=2, n_butacas_largo=3,
                distribucion_por_pelicula=distribucion)
    p = PeliculaFecha(nombre=nombre_pelicula, fecha_lanzamiento=None, genero=None, dia_semana=None, hora=None)
    p_no_existente = PeliculaFecha(nombre=nombre_pelicula_no_existente, fecha_lanzamiento=None, genero=None,
                                   dia_semana=None, hora=None)

    # Act
    distribucion_obtenida = sala.obtener_distribucion_por_pelicula(p)

    # Assert
    assert_that(distribucion[p.nombre]).is_equal_to(distribucion_obtenida)
    assert_that(sala.obtener_distribucion_por_pelicula).raises(CineTicketsException).when_called_with(p_no_existente)


@pytest.mark.parametrize('nombre_pelicula, distribucion_por_pelicula, distribucion_esperada, tamano_nuevo_grupo', [
    (
            'pelicula1',
            {'pelicula1': [['1', '0', '1'], ['0', '0', '0'], ['2', '0', '2']]},
            {'pelicula1': [['1', '0', '1'], ['0', '3', '0'], ['2', '0', '2']]},
            1
    ),
    (
            'pelicula2',
            {'pelicula2': [['1', '0', '1'], ['0', '0', '0'], ['2', '0', '2']]},
            None,
            2
    ),
    (
            'pelicula3',
            {'pelicula3': [['1', '0', '0', '1'], ['0', '0', '0', '0'], ['2', '0', '0', '2']]},
            {'pelicula3': [['1', '0', '0', '1'], ['0', '3', '3', '0'], ['2', '0', '0', '2']]},
            2
    ),
])
def test_anadir_grupo_a_distribucion(nombre_pelicula, distribucion_por_pelicula, distribucion_esperada,
                                     tamano_nuevo_grupo):
    """Prueba la funcion anadir_grupo_a_distribucion dea clase Sala"""
    # Arrange
    p = PeliculaFecha(nombre=nombre_pelicula, fecha_lanzamiento=None, genero=None, dia_semana=None, hora=None)
    sala = Sala(id_sala=1, n_butacas_ancho=3, n_butacas_largo=3,
                distribucion_por_pelicula=distribucion_por_pelicula)

    # Act and Assert
    if distribucion_esperada:
        sala.anadir_grupo_a_distribucion(tamano_nuevo_grupo=tamano_nuevo_grupo, p=p)
        assert_that(sala.obtener_distribucion_por_pelicula(p)).is_equal_to(distribucion_esperada[p.nombre])
    else:
        assert_that(sala.anadir_grupo_a_distribucion).raises(CineTicketsException).when_called_with(tamano_nuevo_grupo,
                                                                                                    p)
