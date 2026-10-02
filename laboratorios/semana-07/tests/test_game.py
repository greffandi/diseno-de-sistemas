import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from game.config import GameConfig
from game.estrategias import AtaqueFuerte, AtaqueNormal
from game.facade import GameFacade
from game.factories import FantasyFactory, PersonajeFactory, SciFiFactory
from game.personajes import Alien, Dragon, Guerrero, Soldado


class ConfigTestCase(unittest.TestCase):
    """Guarda y restaura el estado del Singleton entre pruebas."""

    def setUp(self):
        self.config = GameConfig()
        self._dif = self.config.dificultad
        self._turnos = self.config.numero_maximo_turnos

    def tearDown(self):
        self.config.dificultad = self._dif
        self.config.numero_maximo_turnos = self._turnos


class TestSingleton(ConfigTestCase):
    def test_misma_instancia(self):
        self.assertIs(GameConfig(), GameConfig())

    def test_valores_por_defecto(self):
        self.assertEqual(self.config.dificultad, "normal")
        self.assertEqual(self.config.numero_maximo_turnos, 15)


class TestFactory(unittest.TestCase):
    def test_crea_tipos(self):
        self.assertIsInstance(PersonajeFactory.crear("guerrero"), Guerrero)
        self.assertIsInstance(PersonajeFactory.crear("soldado"), Soldado)
        self.assertIsInstance(PersonajeFactory.crear("Dragon"), Dragon)

    def test_tipo_desconocido(self):
        with self.assertRaises(ValueError):
            PersonajeFactory.crear("mago")


class TestAbstractFactory(unittest.TestCase):
    def test_fantasia(self):
        f = FantasyFactory()
        self.assertIsInstance(f.crear_jugador(), Guerrero)
        self.assertIsInstance(f.crear_enemigo(), Dragon)

    def test_scifi(self):
        f = SciFiFactory()
        self.assertIsInstance(f.crear_jugador(), Soldado)
        self.assertIsInstance(f.crear_enemigo(), Alien)


class TestStrategy(unittest.TestCase):
    def test_ataque_normal(self):
        g, d = Guerrero(), Dragon()
        self.assertEqual(g.atacar(d), 15)
        self.assertEqual(d.vida, 105)

    def test_ataque_fuerte_trunca(self):
        g, d = Guerrero(), Dragon()
        g.set_estrategia(AtaqueFuerte())
        self.assertEqual(g.atacar(d), 22)  # int(15 * 1.5)
        self.assertEqual(d.vida, 98)

    def test_cambio_de_estrategia(self):
        g = Guerrero()
        self.assertIsInstance(g.estrategia, AtaqueNormal)
        g.set_estrategia(AtaqueFuerte())
        self.assertIsInstance(g.estrategia, AtaqueFuerte)


class TestPersonaje(unittest.TestCase):
    def test_vida_no_baja_de_cero(self):
        d = Dragon()
        d.recibir_dano(9999)
        self.assertEqual(d.vida, 0)
        self.assertFalse(d.esta_vivo())


class TestFacade(ConfigTestCase):
    def _jugar(self, respuestas):
        """Ejecuta una partida con respuestas simuladas; devuelve la salida."""
        salida = io.StringIO()
        with patch("builtins.input", side_effect=respuestas), redirect_stdout(salida):
            GameFacade().iniciar()
        return salida.getvalue()

    def test_partida_termina_con_ganador(self):
        texto = self._jugar(["1"] + ["2"] * 20)
        self.assertIn("Ganador: Guerrero", texto)

    def test_partida_scifi(self):
        texto = self._jugar(["2"] + ["2"] * 20)
        self.assertIn("Ganador: Soldado", texto)

    def test_limite_de_turnos_gana_mayor_vida(self):
        self.config.numero_maximo_turnos = 1
        texto = self._jugar(["1", "2"])   # Guerrero 88 vs Dragón 98
        self.assertIn("Ganador: Dragón", texto)

    def test_dificultad_modifica_ataque_enemigo(self):
        self.config.dificultad = "dificil"
        facade = GameFacade()
        with patch("builtins.input", side_effect=["1"]), redirect_stdout(io.StringIO()):
            facade._crear_mundo()
            facade._crear_personajes()
        self.assertEqual(facade._enemigo.ataque, 15)  # int(12 * 1.25)

    def test_empate(self):
        facade = GameFacade()
        facade._jugador, facade._enemigo = Guerrero(), Dragon()
        facade._jugador.vida = facade._enemigo.vida = 50
        with redirect_stdout(io.StringIO()):
            self.assertIsNone(facade._determinar_ganador())


if __name__ == "__main__":
    unittest.main()
