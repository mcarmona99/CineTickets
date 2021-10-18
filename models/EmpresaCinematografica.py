from typing import Union

from Pelicula import Pelicula


class EmpresaCinematografica:
    """Modelo EmpresaCinematográfica."""

    def __init__(self, nombre: str, peliculas: Union[list, None] = None, salas: Union[list, None] = None):
        """Inicializa un objeto de la clase EmpresaCinematografica.

        Parameters
        ----------
        nombre : str
            Nombre de la empresa cinematográfica que representa el objeto.
        peliculas : Union[list, None]
            Lista de películas ofertadas por la empresa cinematográfica.

        Returns
        -------
        object
            Objeto de la clase EmpresaCinematografica.
        """
        self.nombre = nombre
        self.peliculas = peliculas if peliculas else []
        self.salas = salas if salas else []

    def anadir_pelicula(self, p: Pelicula, parametros: dict):
        """Añade una película a la lista de películas del cine.

        Parameters
        ----------
        p : Pelicula
            Objeto que representa la película a añadir a la lista de películas del cine.
        parametros : dict
            Variable de tipo diccionario que incluye parámetros para la creación de objetos PeliculaFecha a añadir.
        """
        raise NotImplementedError

    def modificar_pelicula(self, p: Pelicula, parametros: dict):
        """Modifica una película de la lista de películas del cine.

        Parameters
        ----------
        p : Pelicula
            Objeto que representa la película a modificar de la lista de películas del cine.
        parametros : dict
            Variable de tipo diccionario que incluye parámetros para la modificación de objetos PeliculaFecha del cine.
        """
        raise NotImplementedError

    def eliminar_pelicula(self, p: Pelicula):
        """Elimina una película de la lista de películas del cine.

        Parameters
        ----------
        p : Pelicula
            Objeto que representa la película a eliminar de la lista de películas del cine.
        """
        raise NotImplementedError
