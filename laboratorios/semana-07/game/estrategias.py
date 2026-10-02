"""Patrón Strategy: formas de atacar intercambiables en tiempo de ejecución."""
from abc import ABC, abstractmethod


class EstrategiaAtaque(ABC):
    nombre = "Estrategia"

    @abstractmethod
    def ejecutar(self, atacante, objetivo) -> int:
        """Aplica el ataque al objetivo y devuelve el daño causado."""


class AtaqueNormal(EstrategiaAtaque):
    nombre = "Ataque normal"

    def ejecutar(self, atacante, objetivo) -> int:
        dano = atacante.ataque
        objetivo.recibir_dano(dano)
        return dano


class AtaqueFuerte(EstrategiaAtaque):
    nombre = "Ataque fuerte"

    def ejecutar(self, atacante, objetivo) -> int:
        dano = int(atacante.ataque * 1.5)
        objetivo.recibir_dano(dano)
        return dano
