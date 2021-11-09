from typing import Union

from cinetickets.CineTicketsException import CineTicketsException
from cinetickets.Pelicula import PeliculaFecha


class Sala:
    """Modelo Sala."""

    def __init__(self, id_sala: int, n_butacas_ancho: int, n_butacas_largo: int,
                 distribucion_por_pelicula: Union[dict, None] = None):
        """Inicializa un objeto de la clase Sala.

        Parameters
        ----------
        id_sala : int
            Identificador de la sala.
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

        Raises
        ------
        CineTicketsException
            Excepción levantada si no tenemos distribución para la película elegida.

        Returns
        -------
        list
            Lista de listas que representa una matriz ilustrando la distribución actual de la sala para la película en
            cuestión.
        """
        nombre_pelicula = p.nombre
        distribucion = self.distribucion_por_pelicula.get(nombre_pelicula)
        if not distribucion:
            raise CineTicketsException(codigo=1)
        return distribucion

    def anadir_grupo_a_distribucion(self, tamano_nuevo_grupo: int, p: PeliculaFecha):
        """Añade un nuevo grupo a una distribución de butacas para una película, respetando restricciones.

        Parameters
        ----------
        tamano_nuevo_grupo : int
            Tamaño del nuevo grupo a añadir a la distribución.
        p : PeliculaFecha
            Pelicula a la que queremos añadir el grupo a su distribución.
        """
        distribucion_pelicula = self.obtener_distribucion_por_pelicula(p)

        # El grupo a añadir es identificado por la variable nueva_etiqueta
        filas_unificadas = []
        for fila in distribucion_pelicula:
            filas_unificadas.extend(fila)
        nueva_etiqueta = str(max([int(f) for f in filas_unificadas]) + 1)

        for indice_fila, fila in enumerate(distribucion_pelicula):
            fila_string = "".join(fila)
            # Añado el char | para indicar tope de fila
            fila_string = f"|{fila_string}|"

            # Variables para indicar la posicion del hueco
            pegado_izquierda, pegado_derecha = False, False

            # Comprobar tamaño del hueco
            indice_hueco = fila_string.find('0')
            tamano_hueco = 1
            while fila_string[indice_hueco + tamano_hueco] == '0':
                tamano_hueco += 1

            # Hueco no pegado a paredes
            if not any([pegado_derecha, pegado_izquierda]) and tamano_hueco >= tamano_nuevo_grupo + 2:
                # Antes de meter el grupo a fila, compruebo las filas arriba y abajo
                if indice_fila == 0:
                    check = all([distribucion_pelicula[indice_fila + 1][indice_hueco + i] == '0' for i in
                                 range(0, tamano_nuevo_grupo)])
                elif indice_fila == len(fila) - 1:
                    check = all([distribucion_pelicula[indice_fila - 1][indice_hueco + i] == '0' for i in
                                 range(0, tamano_nuevo_grupo)])
                else:
                    check = all([distribucion_pelicula[indice_fila - 1][indice_hueco + i] == '0' for i in
                                 range(0, tamano_nuevo_grupo)]) and all(
                        [distribucion_pelicula[indice_fila + 1][indice_hueco + i] == '0' for i in
                         range(0, tamano_nuevo_grupo)])
                if check:
                    # Meto el grupo en la fila
                    fila_nueva = [f for f in fila_string if f != '|']
                    for i in range(0, tamano_nuevo_grupo):
                        fila_nueva[indice_hueco + i] = nueva_etiqueta
                    self.distribucion_por_pelicula[p.nombre][indice_fila] = fila_nueva
                    return

        raise CineTicketsException(2)

    def redistribuir_butacas(self, tamano_nuevo_grupo: int):
        """Aplica una función heurística para buscar una nueva distribución de butacas que permita meter a un nuevo
        grupo, respetando restricciones.

        Parameters
        ----------
        tamano_nuevo_grupo : int
            Tamaño del nuevo grupo a añadir a la distribución.
        """
        raise NotImplementedError
