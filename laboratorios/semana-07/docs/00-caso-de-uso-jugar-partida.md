# Caso de uso: Jugar partida

**Actor:** Jugador

**Flujo principal**
1. El jugador selecciona un mundo (Fantasía o Ciencia ficción).
2. El sistema crea la fábrica del mundo, el jugador y el enemigo.
3. El sistema establece la estrategia inicial del jugador (ataque normal).
4. En cada turno, el jugador puede mantener o cambiar su estrategia (ataque normal o ataque fuerte).
5. El jugador ataca al enemigo con la estrategia seleccionada.
6. Si el enemigo sigue vivo, el enemigo responde atacando al jugador.
7. El sistema comprueba la vida de ambos personajes.
8. El proceso continúa hasta que un personaje llegue a 0 de vida o se alcance el número máximo de turnos configurado.
9. El sistema determina y muestra el resultado.

**Regla al alcanzar el máximo de turnos:** gana el personaje con más vida; si tienen la misma vida, hay empate.
