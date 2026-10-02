# Taller Integrador: Videojuego por turnos

Juego de combate por turnos en consola (jugador vs enemigo) que aplica los patrones
Factory, Abstract Factory, Strategy, Facade y Singleton.

## Ejecución

```bash
docker build -t game-patterns .
docker run --rm -it game-patterns     # interactivo (recomendado)
docker run --rm game-patterns         # sin teclado: usa opciones por defecto
```

Sin Docker: `python main.py`. Pruebas: `python -m unittest -v`.

## Patrones y dónde están

| Patrón | Clases | Archivo |
|---|---|---|
| Factory | `PersonajeFactory.crear("guerrero")` | `game/factories.py` |
| Abstract Factory | `MundoFactory`, `FantasyFactory`, `SciFiFactory` | `game/factories.py` |
| Strategy | `EstrategiaAtaque`, `AtaqueNormal`, `AtaqueFuerte` | `game/estrategias.py` |
| Singleton | `GameConfig` | `game/config.py` |
| Facade | `GameFacade` | `game/facade.py` |

`main.py` solo crea `GameFacade` y llama a `iniciar()`.
Las fábricas concretas crean sus personajes a través de `PersonajeFactory`.

## Mundos y personajes

| Mundo | Jugador | Enemigo |
|---|---|---|
| Fantasía | Guerrero (vida 100, ataque 15) | Dragón (vida 120, ataque 12) |
| Ciencia ficción | Soldado (vida 90, ataque 14) | Alien (vida 110, ataque 13) |

## Reglas

- **Turno:** el jugador elige o mantiene su estrategia (puede cambiarla en cada turno), ataca y, si el enemigo sigue vivo, el enemigo responde. El enemigo siempre usa ataque normal.
- **Ataque normal:** causa el valor de ataque del personaje.
- **Ataque fuerte:** causa 150 % del ataque, truncado a entero (Guerrero: 15 → 22).
- **Fin de la partida:** termina cuando un personaje llega a 0 de vida o cuando se alcanza `numero_maximo_turnos` (por defecto 15).
- **Límite de turnos (regla de diseño del equipo):** el enunciado no indica qué pasa si se agotan los turnos. Se definió que gana quien tenga más vida y, si es igual, hay empate.
- **Dificultad (`GameConfig.dificultad`, por defecto `normal`):** multiplica el ataque del enemigo: fácil ×0.75, normal ×1.0, difícil ×1.25. No hay menú para cambiarla; se modifica en `GameConfig`.

## Diagramas (`/docs`, PlantUML)

- `00-caso-de-uso-jugar-partida.md`: descripción del caso de uso
- `01-casos-de-uso.puml`
- `02-dominio.puml`
- `03-robustez-jugar-partida.puml`
- `04-secuencia-turno.puml`
