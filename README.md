# -videojuego-laberinto

# Laberinto

Este proyecto implementa un juego de laberinto en Python utilizando programación orientada a objetos. El juego permite al jugador moverse por un laberinto representado por un mapa y alcanzar la salida.

## Funcionalidades

- El jugador puede moverse hacia arriba (W), abajo (S) izquierda (A) o derecha (D) en el laberinto.
- El juego termina cuando el jugador alcanza la salida del laberinto.
- El juego utiliza archivos de texto para cargar laberintos aleatorios desde una carpeta.

## Instrucciones de Ejecución

1. Clona este repositorio en tu máquina local.
   git clone https://github.com/Abneriz/Proyecto1.git
   
3. Asegúrate de tener Python instalado en tu sistema.
4. Ejecuta el script `main.py` para comenzar el juego.
5. Sigue las instrucciones en pantalla para mover al jugador por el laberinto.
6. El objetivo es llegar a la salida del laberinto antes de que el jugador se quede sin movimientos.

## Estructura de Archivos

- `main.py`: El punto de entrada del programa.
- `juego.py`: Contiene la implementación de las clases `Juego` y `JuegoArchivo`.
- `mapa.txt`: Un ejemplo de archivo de mapa utilizado en el juego.
- `carpeta_de_mapas/`: Carpeta que contiene varios archivos de mapas para el juego.

## Ejemplo de Mapa

El formato de los archivos de mapa es el siguiente:

README - Juego de Laberinto
Este proyecto consiste en un juego de laberinto desarrollado en Python, donde el jugador debe mover un personaje (representado por 'P') desde una posición inicial hasta una posición final ('F') evitando obstáculos ('#'). El jugador puede moverse al personaje utilizando las teclas de dirección.

Funcionalidades
Movimiento del personaje: El jugador puede mover el personaje hacia arriba, abajo, izquierda o derecha utilizando las teclas de dirección.
Generación Aleatoria de Laberintos: El juego puede cargar laberintos aleatorios desde archivos de mapa en una carpeta específica.
Jugabilidad interactiva: El juego proporciona una interfaz interactiva donde el jugador puede moverse por el laberinto y completarlo.
Contador de Números: Presionando la tecla 'N', se activa un contador que suma números mientras la tecla esté presionada.
Mensajes de Estado: El juego proporciona mensajes de estado al jugador, como bienvenida, indicaciones para comenzar y felicitaciones al completar el laberinto.
Requisitos
Pitón 3.x
Libreríareadchar
Sistema Operativo: Windows o Unix (Linux/macOS)
Instrucciones de uso
Clonar el Repositorio: Clona el repositorio en tu máquina local.
git clone https://github.com/Abneriz/Proyecto1.git
1 Instalar Dependencias: Instala las dependencias requeridas ejecutando el siguiente comando en la terminal:

pip install readchar
Ejecutar el juego: Ejecuta el script principal laberinto.pypara iniciar el juego.
python laberinto.py
Jugar: Sigue las instrucciones en pantalla para mover al personaje por el laberinto y completarlo.
Estructura del Proyecto
El proyecto está organizado de la siguiente manera:

laberinto.py: Contiene el código principal del juego.
carpeta_mapas/: Carpeta que contiene archivos de mapas de laberintos.
README.md: Este archivo que proporciona información sobre el juego y cómo usarlo.
Notas adicionales
Asegúrese de tener los permisos necesarios para ejecutar scripts en su sistema operativo.
Puedes agregar tus propios mapas de laberinto en la carpeta carpeta_mapas/siguiendo el formato especificado en el código.
¡Disfruta del juego y buena suerte en la aventura del laberinto! 🎮🔍.
