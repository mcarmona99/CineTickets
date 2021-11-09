class CineTicketsException(Exception):
    ERROR_CODES_DESCRIPTION = {
        1: "No hay pelicula disponible asociada al nombre dado",
        2: "El grupo no puede ser añadido a la distribución",
    }

    MENSAJE_ERROR_NO_EXISTENTE = 'Sin mensaje para este código de error'

    def __init__(self, codigo):
        super().__init__()
        self.codigo = codigo
        self.mensaje = self.ERROR_CODES_DESCRIPTION.get(codigo, self.MENSAJE_ERROR_NO_EXISTENTE)
