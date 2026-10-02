"""Patrón Facade: único punto de acceso para jugar una partida.

Reglas del juego:
- Cada turno: el jugador elige (o mantiene) su estrategia, ataca, y si el
  enemigo sigue vivo, el enemigo responde.
- La partida termina cuando un personaje llega a 0 de vida o cuando se
  alcanza GameConfig.numero_maximo_turnos.
- Si se alcanza el límite de turnos, gana quien tenga más vida; si la vida
  es igual, hay empate.
- La dificultad multiplica el ataque del enemigo (facil 0.75, normal 1.0,
  dificil 1.25).
"""
from game.config import GameConfig
from game.estrategias import AtaqueFuerte, AtaqueNormal
from game.factories import FantasyFactory, MundoFactory, SciFiFactory
from game.personajes import Personaje


class GameFacade:
    MUNDOS = {"1": FantasyFactory, "2": SciFiFactory}
    ESTRATEGIAS = {"1": AtaqueNormal, "2": AtaqueFuerte}
    FACTOR_DIFICULTAD = {"facil": 0.75, "normal": 1.0, "dificil": 1.25}

    def __init__(self):
        self._config = GameConfig()
        self._fabrica: MundoFactory | None = None
        self._jugador: Personaje | None = None
        self._enemigo: Personaje | None = None

    # ---------- API pública ----------
    def iniciar(self) -> None:
        self._crear_mundo()
        self._crear_personajes()
        self._ejecutar_turnos()
        self._determinar_ganador()

    # ---------- 1. Crear el mundo ----------
    def _crear_mundo(self) -> None:
        print("=== Videojuego por turnos ===")
        print("Selecciona un mundo:\n  1. Fantasía (Guerrero vs Dragón)\n  2. Ciencia ficción (Soldado vs Alien)")
        opcion = self._leer("Mundo [1-2] (Enter = 1): ", self.MUNDOS, "1")
        self._fabrica = self.MUNDOS[opcion]()
        print(f"\nMundo: {self._fabrica.nombre}")

    # ---------- 2. Crear jugador y enemigo ----------
    def _crear_personajes(self) -> None:
        self._jugador = self._fabrica.crear_jugador()
        self._enemigo = self._fabrica.crear_enemigo()
        factor = self.FACTOR_DIFICULTAD[self._config.dificultad]
        self._enemigo.ataque = int(self._enemigo.ataque * factor)
        print(f"Dificultad: {self._config.dificultad} | Turnos máximos: {self._config.numero_maximo_turnos}")
        self._mostrar_estado()

    # ---------- 3 y 4. Ejecutar turnos y aplicar estrategia ----------
    def _ejecutar_turnos(self) -> None:
        for turno in range(1, self._config.numero_maximo_turnos + 1):
            print(f"\n--- Turno {turno} ---")
            self._elegir_estrategia()
            self._turno_jugador()
            if not self._enemigo.esta_vivo():
                break
            self._turno_enemigo()
            self._mostrar_estado()
            if not self._jugador.esta_vivo():
                break

    def _elegir_estrategia(self) -> None:
        actual = self._jugador.estrategia.nombre
        print(f"Estrategia actual: {actual}\n  1. Ataque normal\n  2. Ataque fuerte")
        opcion = self._leer("Elige [1-2] (Enter = mantener): ", self.ESTRATEGIAS, "")
        if opcion:
            self._jugador.set_estrategia(self.ESTRATEGIAS[opcion]())

    def _turno_jugador(self) -> None:
        dano = self._jugador.atacar(self._enemigo)
        print(f"{self._jugador.nombre} usa {self._jugador.estrategia.nombre} y causa {dano} de daño.")
        if not self._enemigo.esta_vivo():
            self._mostrar_estado()

    def _turno_enemigo(self) -> None:
        dano = self._enemigo.atacar(self._jugador)
        print(f"{self._enemigo.nombre} responde y causa {dano} de daño.")

    # ---------- 5. Determinar ganador ----------
    def _determinar_ganador(self) -> Personaje | None:
        j, e = self._jugador, self._enemigo
        if not e.esta_vivo():
            ganador = j
        elif not j.esta_vivo():
            ganador = e
        elif j.vida != e.vida:                      # se acabaron los turnos
            ganador = j if j.vida > e.vida else e
        else:
            ganador = None
        print("\n=== Fin del combate ===")
        print(f"Ganador: {ganador.nombre}" if ganador else "Resultado: empate")
        return ganador

    # ---------- utilidades de consola ----------
    def _mostrar_estado(self) -> None:
        for p in (self._jugador, self._enemigo):
            print(f"  {p.nombre}: vida {p.vida} | ataque {p.ataque}")

    @staticmethod
    def _leer(mensaje: str, validas, defecto: str) -> str:
        while True:
            try:
                texto = input(mensaje).strip()
            except EOFError:                        # sin terminal interactiva (docker run sin -it)
                print(f"(sin entrada: se usa '{defecto or 'mantener'}')")
                return defecto
            if texto == "":
                return defecto
            if texto in validas:
                return texto
            print("Opción inválida.")
