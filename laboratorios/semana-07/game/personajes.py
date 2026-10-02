"""Dominio: personajes del juego (nombre, vida, ataque)."""
from game.estrategias import AtaqueNormal, EstrategiaAtaque


class Personaje:
    def __init__(self, nombre: str, vida: int, ataque: int):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.estrategia: EstrategiaAtaque = AtaqueNormal()

    def set_estrategia(self, estrategia: EstrategiaAtaque) -> None:
        self.estrategia = estrategia

    def atacar(self, objetivo: "Personaje") -> int:
        return self.estrategia.ejecutar(self, objetivo)

    def recibir_dano(self, dano: int) -> None:
        self.vida = max(0, self.vida - dano)

    def esta_vivo(self) -> bool:
        return self.vida > 0


class Guerrero(Personaje):
    def __init__(self):
        super().__init__("Guerrero", vida=100, ataque=15)


class Dragon(Personaje):
    def __init__(self):
        super().__init__("Dragón", vida=120, ataque=12)


class Soldado(Personaje):
    def __init__(self):
        super().__init__("Soldado", vida=90, ataque=14)


class Alien(Personaje):
    def __init__(self):
        super().__init__("Alien", vida=110, ataque=13)
