from datetime import datetime

from cinetickets.Sala import Sala


class Pelicula:
    """Modelo Pelicula."""

    def __init__(self, nombre: str, fecha_lanzamiento: datetime, genero: str):
        """Inicializa un objeto de la clase Pelicula.

        Parameters
        ----------
        nombre : str
            Nombre de la pelicula.
        fecha_lanzamiento : datetime
            Fecha de estreno de la película en cines.
        genero : str
            Género al que pertenece la película representada por el objeto.

        Returns
        -------
        object
            Objeto de la clase Pelicula.
        """
        self.nombre = nombre
        self.fecha_lanzamiento = fecha_lanzamiento
        self.genero = genero


class PeliculaFecha(Pelicula):
    """Modelo PeliculaFecha."""

    def __init__(self, nombre: str, fecha_lanzamiento: datetime, genero: str, fecha_proyeccion: datetime,
                 sala_proyeccion: Sala, distribucion: list = None):
        """Inicializa un objeto de la clase PeliculaFecha.

        Parameters
        ----------
        nombre : str
            Nombre de la pelicula.
        fecha_lanzamiento : datetime
            Fecha de estreno de la película en cines.
        genero : str
            Género al que pertenece la película representada por el objeto.
        fecha_proyeccion : datetime
            Fecha y hora en la que se emitirá esta película.
        sala_proyeccion : Sala
            Sala en la que se emitirá esta película
        distribucion : list
            Distribucion de butacas la pelicula, por defecto vacía.

        Returns
        -------
        object
            Objeto de la clase PeliculaFecha.
        """
        super().__init__(nombre=nombre, fecha_lanzamiento=fecha_lanzamiento, genero=genero)
        self.fecha_proyeccion = fecha_proyeccion
        self.sala_proyeccion = sala_proyeccion
        if not distribucion:
            self.inicializar_distribucion()
        else:
            self.distribucion = distribucion

    def inicializar_distribucion(self):
        """Inicializa la distribución de la película como una sala vacía."""
        self.distribucion = [[0 for _ in range(self.sala_proyeccion.n_butacas_ancho)] for _ in
                             range(self.sala_proyeccion.n_butacas_largo)]

    def anadir_grupo_a_distribucion(self, tamano_nuevo_grupo: int):
        """Añade un nuevo grupo a la distribución de butacas de la película, respetando restricciones.

        Parameters
        ----------
        tamano_nuevo_grupo : int
            Tamaño del nuevo grupo a añadir a la distribución.
        """
        # El grupo a añadir es identificado por la variable nueva_etiqueta
        filas_unificadas = []
        for fila in self.distribucion:
            filas_unificadas.extend(fila)
        nueva_etiqueta = str(max([int(f) for f in filas_unificadas]) + 1)

        for indice_fila, fila in enumerate(self.distribucion):
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
                    check = all([self.distribucion[indice_fila + 1][indice_hueco + i] == '0' for i in
                                 range(0, tamano_nuevo_grupo)])
                elif indice_fila == len(fila) - 1:
                    check = all([self.distribucion[indice_fila - 1][indice_hueco + i] == '0' for i in
                                 range(0, tamano_nuevo_grupo)])
                else:
                    check = all([self.distribucion[indice_fila - 1][indice_hueco + i] == '0' for i in
                                 range(0, tamano_nuevo_grupo)]) and all(
                        [self.distribucion[indice_fila + 1][indice_hueco + i] == '0' for i in
                         range(0, tamano_nuevo_grupo)])
                if check:
                    # Meto el grupo en la fila
                    fila_nueva = [f for f in fila_string if f != '|']
                    for i in range(0, tamano_nuevo_grupo):
                        fila_nueva[indice_hueco + i] = nueva_etiqueta
                    self.distribucion[indice_fila] = fila_nueva
                    return

    def redistribuir_butacas(self, tamano_nuevo_grupo: int):
        """Aplica una función heurística para buscar una nueva distribución de butacas que permita meter a un nuevo
        grupo, respetando restricciones.

        Parameters
        ----------
        tamano_nuevo_grupo : int
            Tamaño del nuevo grupo a añadir a la distribución.
        """
        raise NotImplementedError
