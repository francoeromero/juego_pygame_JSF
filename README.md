
## UTN AVELLANEDA - Tecnicatura Universitaria en Programación

DIV 313-2  
Grupo JSF - **J**ulian Ortiz - **S**ebastian Lescano - **F**ranco Romero  
Proyecto: Pregunta y gool!  
Docente: Mariano Fernandez  

---
![Portada](./img/readme/readme_portada.jpg)
**Pregunta y Gool!** es un juego de preguntas y respuestas basado en la popular dinámica de **Preguntados** con una temática futbolista, desarrollado en Python utilizando la biblioteca **Pygame**. El juego incluye características como preguntas aleatorias, comodines, gestión de puntajes y configuración personalizada.

---
# Idea Principal del Juego
![Portada](./img/readme/idea_general.png)
La idea principal del juego es generar una experiencia visual atractiva y dinámica a través de la simulación de **profundidad de campo**, estructurada en **tres planos** visuales claramente diferenciados:

## 1. Primer Plano (Animado y Fuera de Contexto)
![Portada](./img/readme/primer_plano.png)
Este plano se sitúa al fondo de la ventana de Pygame y está compuesto por elementos animados que, aunque no están directamente relacionados con la narrativa del juego, generan una sensación de profundidad y movimiento. Este fondo dinámico aporta riqueza visual y crea una atmósfera inmersiva, destacando la tridimensionalidad de la escena.

## 2. Segundo Plano (Fijo)
![Portada](./img/readme/segundo_plano.png)
En este plano, se representa una computadora portátil con su pantalla abierta. En la pantalla se desarrolla la interfaz principal del juego. Este elemento actúa como un marco intermedio fijo, estableciendo un contraste con el dinamismo del primer plano. Este recurso enfatiza la idea de que el jugador interactúa dentro de un entorno enmarcado, aportando un toque visual único.

## 3. Tercer Plano (Protagonista y Nivel)
![Portada](./img/readme/tercer_plano.png)
Este es el plano más cercano al jugador y representa al protagonista del juego. A medida que el jugador avanza por los niveles, el protagonista cambia, reflejando el progreso en el juego. Sin embargo, el segundo plano (la computadora) y el primer plano (fondo animado) permanecen constantes, reforzando la idea de continuidad en la experiencia visual. El contraste entre el dinamismo del primer plano, la estabilidad del segundo, y la evolución en el tercer plano genera un equilibrio visual que mantiene al jugador inmerso en la experiencia.

---

## Objetivo Visual y Narrativo
![Portada](./img/readme/menu_principal.png)
El diseño busca unir elementos de **interactividad** y **narrativa visual** en una estructura única. La combinación de planos fijos y dinámicos no solo añade profundidad, sino que también guía la atención del jugador hacia el desarrollo del juego en el tercer plano, mientras los otros planos complementan la experiencia de forma armoniosa.
![Portada](./img/readme/nivel1.png)
![Portada](./img/readme/nivel2.png)
![Portada](./img/readme/nivel3.png)
![Portada](./img/readme/nivel4.png)
![Portada](./img/readme/nivel5.png)
![Portada](./img/readme/nivel6.png)
---
## **Características Principales**
- **Modo de Juego:**
  - Preguntas aleatorias tomadas de un archivo `preguntas.csv`.
  - Cuatro opciones de respuesta por pregunta.
  - Gestión de vidas y puntos: pierdes vidas al responder mal y ganas puntos al acertar.
  - Bonus: Responder correctamente 5 veces seguidas otorga una vida adicional.

- **Comodines Disponibles:**
  - **Bomba**: Elimina dos respuestas incorrectas.
  - **X2**: Duplica los puntos obtenidos al acertar.
  - **Doble Oportunidad**: Permite una segunda respuesta en caso de errar.
  - **Pasar**: Avanza a la siguiente pregunta sin afectar el puntaje ni las vidas.

- **Sistema de Tiempo:**
  - Opción de tiempo por pregunta o tiempo total para la partida.
  - Gana tiempo adicional respondiendo 5 preguntas consecutivas correctamente.

- **Fin de la Partida:**
  - Registro del nombre del jugador, puntaje y fecha en `partidas.json`.

- **Ranking TOP 10:**
  - Visualiza las 10 partidas con mayor puntaje.

- **Opciones de Configuración:**
  - Ajuste de música (activar/desactivar, control de volumen).
  - Modificación de parámetros del juego (vidas, puntos, tiempo, etc.).

- **Estadísticas:**
  - Registro de datos como porcentaje de aciertos, cantidad de fallos y veces que una pregunta ha sido respondida.

---

## **Requisitos del Sistema**
- Python 3.10+
- Biblioteca **Pygame** instalada (v2.0+)
- Archivos necesarios:
  - `preguntas.csv`: Contiene las preguntas y respuestas.
  - `partidas.json`: Registro de partidas jugadas.

---

## **Instalación**
1. Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/pregunta-y-gool.git

2. Navega al directorio del proyecto:
    ```bash
    cd pregunta-y-gool
3. Instala las dependencias necesarias:
    ```bash
    pip install pygame
4. Inicia el juego:
    ```bash
    python Principal.py
