from datetime import datetime, time


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

    def __init__(self, nombre: str, fecha_lanzamiento: datetime, genero: str, dia_semana: str, hora: time):
        """Inicializa un objeto de la clase PeliculaFecha.

        Parameters
        ----------
        nombre : str
            Nombre de la pelicula.
        fecha_lanzamiento : datetime
            Fecha de estreno de la película en cines.
        genero : str
            Género al que pertenece la película representada por el objeto.
        dia_semana : str
            Día de la semana en el que se emitirá esta película.
        hora : time
            Hora a la que se emitirá esta película, en el dia de la semana especificado.

        Returns
        -------
        object
            Objeto de la clase PeliculaFecha.
        """
        super().__init__(nombre=nombre, fecha_lanzamiento=fecha_lanzamiento, genero=genero)
        self.dia_semana = dia_semana
        self.hora = hora
