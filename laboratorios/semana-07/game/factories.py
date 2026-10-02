"""Patrones Factory y Abstract Factory."""
from abc import ABC, abstractmethod

from game.personajes import Alien, Dragon, Guerrero, Personaje, Soldado


class PersonajeFactory:
    """Factory: crea un personaje a partir de su tipo."""

    _TIPOS = {
        "guerrero": Guerrero,
        "dragon": Dragon,
        "soldado": Soldado,
        "alien": Alien,
    }

    @staticmethod
    def crear(tipo: str) -> Personaje:
        try:
            return PersonajeFactory._TIPOS[tipo.lower()]()
        except KeyError:
            raise ValueError(f"Tipo de personaje desconocido: {tipo}")


class MundoFactory(ABC):
    """Abstract Factory: crea la familia de personajes de un mundo."""

    nombre = "Mundo"

    @abstractmethod
    def crear_jugador(self) -> Personaje: ...

    @abstractmethod
    def crear_enemigo(self) -> Personaje: ...


class FantasyFactory(MundoFactory):
    nombre = "Fantasía"

    def crear_jugador(self) -> Personaje:
        return PersonajeFactory.crear("guerrero")

    def crear_enemigo(self) -> Personaje:
        return PersonajeFactory.crear("dragon")


class SciFiFactory(MundoFactory):
    nombre = "Ciencia ficción"

    def crear_jugador(self) -> Personaje:
        return PersonajeFactory.crear("soldado")

    def crear_enemigo(self) -> Personaje:
        return PersonajeFactory.crear("alien")
