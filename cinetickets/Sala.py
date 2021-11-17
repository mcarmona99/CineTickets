class Sala:
    """Modelo Sala."""

    def __init__(self, id_sala: int, n_butacas_ancho: int, n_butacas_largo: int):
        """Inicializa un objeto de la clase Sala.

        Parameters
        ----------
        id_sala : int
            Identificador de la sala.
        n_butacas_ancho : int
            Número de butacas de la sala por fila.
        n_butacas_largo : str
            Número de butacas de la sala por columna.

        Returns
        -------
        object
            Objeto de la clase Sala.
        """
        self.id_sala = id_sala
        self.n_butacas_ancho = n_butacas_ancho
        self.n_butacas_largo = n_butacas_largo
