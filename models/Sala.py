from typing import Union

from models.Pelicula import PeliculaFecha


class Sala:
    """Modelo Sala."""

    def __init__(self, id_sala: int, n_butacas_ancho: int, n_butacas_largo: int,
                 distribucion_por_pelicula: Union[dict, None] = None):
        """Inicializa un objeto de la clase Sala.

        Parameters
        ----------
        id_sala : int
            Nombre de la pelicula.
        n_butacas_ancho : int
            Número de butacas de la sala por fila.
        n_butacas_largo : str
            Número de butacas de la sala por columna.
        distribucion_por_pelicula : Union[dict, None]
            Diccionario que representa a cada película que se puede ver en la sala para una fecha y horas determinadas,
            con su respectiva distribución.

        Returns
        -------
        object
            Objeto de la clase Sala.
        """
        self.id_sala = id_sala
        self.n_butacas_ancho = n_butacas_ancho
        self.n_butacas_largo = n_butacas_largo
        self.distribucion_por_pelicula = distribucion_por_pelicula if distribucion_por_pelicula else {}

    def obtener_distribucion_por_pelicula(self, p: PeliculaFecha) -> list:
        """Obteniene la distribucion de la sala para una película específica.

        Parameters
        ----------
        p : PeliculaFecha
            Objeto de la clase PeliculaFecha de la que queremos obtener la distribución.

        Returns
        -------
        list
            Lista de listas que representa una matriz ilustrando la distribución actual de la sala para la película en
            cuestión.
        """
        raise NotImplementedError

    def anadir_grupo_a_distribucion(self, tamano_nuevo_grupo: int, p: PeliculaFecha):
        """Añade un nuevo grupo a una distribución de butacas para una película, respetando restricciones.

        Parameters
        ----------
        tamano_nuevo_grupo : int
            Tamaño del nuevo grupo a añadir a la distribución.
        p : PeliculaFecha
            Pelicula a la que queremos añadir el grupo a su distribución.
        """
        raise NotImplementedError

    def redistribuir_butacas(self, tamano_nuevo_grupo: int, p: PeliculaFecha):
        """Aplica una función heurística para buscar una nueva distribución de butacas que permita meter a un nuevo
        grupo, respetando restricciones.

        Parameters
        ----------
        tamano_nuevo_grupo : int
            Tamaño del nuevo grupo a añadir a la distribución.
        p : PeliculaFecha
            Pelicula a la que queremos añadir el grupo a su distribución.
        """
        raise NotImplementedError
