"""Patrón Singleton: una única instancia de GameConfig."""


class GameConfig:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            instancia = super().__new__(cls)
            instancia.dificultad = "normal"        # facil | normal | dificil
            instancia.numero_maximo_turnos = 15
            cls._instancia = instancia
        return cls._instancia
