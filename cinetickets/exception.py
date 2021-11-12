class CineTicketsClientError(Exception):
    """Clase que instancia las excepciones referentes a respuestas originadas por un error del cliente."""

    def __init__(self, msg: str):
        """Constructor de la clase.

        Parameters
        ----------
        msg : str
            Mensaje de la excepción.
        """
        super().__init__(f'CLIENT ERROR: {msg}')


class CineTicketsServerError(Exception):
    """Clase que instancia las excepciones referentes a respuestas originadas por un error del servidor."""

    def __init__(self, msg: str):
        """Constructor de la clase.

        Parameters
        ----------
        msg : str
            Mensaje de la excepción.
        """
        super().__init__(f'SERVER ERROR: {msg}')


class CineTicketsNotFound(CineTicketsClientError):
    """Error referente a peticiones de recursos no encontrados."""

    def __init__(self, recurso: object):
        """Constructor de la clase.

        Parameters
        ----------
        recurso : object
            Recurso no encontrado.
        """
        super().__init__(
            f'Recurso no encontrado: '
            f'{recurso if isinstance(recurso, str) else f"{type(recurso)} con atributos {recurso.__dict__}"}')
        self.code = 404
