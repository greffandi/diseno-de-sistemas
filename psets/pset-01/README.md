# PSet 1: Análisis y Diseño de ReservaU

**Curso:** Diseño de Sistemas
**Estudiante:** Andrés Greffa (00331611)
**Institución:** Universidad San Francisco de Quito (USFQ)

**Descripción**
Este proyecto contiene los requerimientos, diagramas de casos de uso, flujos, el modelo de dominio y la implementación orientada a objetos (POO) en Python para la plataforma de reservas deportivas ReservaU.

**Estructura del Proyecto**
* Los documentos de diseño en PDF se encuentran en la raíz de esta carpeta.
* El código fuente (`modelo.py` y `simulacion.py`) y el entorno virtualizado están en la subcarpeta `implementacion/`.

**Ejecución de la Simulación con Docker**
Para validar la lógica de reservas, reglas de prioridad y colisiones, navega a la carpeta `implementacion/` y ejecuta los siguientes comandos:

1. **Construir la imagen:**
   ```bash
   docker build -t reservau .