from datetime import time


class ClienteCine:
    """Modelo ClienteCine."""

    def __init__(self, id_usuario: int):
        """Inicializa un objeto de la clase ClienteCine.

        Parameters
        ----------
        id_usuario : int
            Identificador del cliente.

        Returns
        -------
        object
            Objeto de la clase ClienteCine.
        """
        self.id_usuario = id_usuario

    def ver_catalogo(self, filtros: dict) -> list:
        """Devuelve el catálogo de películas disponibles según filtros establecidos.

        Parameters
        ----------
        filtros : dict
            Filtros incluidos en la búsqueda a realizar en el catálogo.

        Returns
        -------
        list
            Catálogo de películas.
        """
        raise NotImplementedError

    def comprar_entradas(self, nombre_pelicula: str, dia_semana: str, hora: time, numero_entradas: int):
        """Añade un nuevo grupo a una distribución de butacas para una película, respetando restricciones.

        Parameters
        ----------
        nombre_pelicula : str
            Nombre de la película para la que se quiere comprar entradas.
        dia_semana : str
            Dia para el que se quieren comprar entradas.
        hora : time
            Hora para la que se quieren comprar entradas.
        numero_entradas : int
            Número de entradas a reservar.
        """
        raise NotImplementedError
