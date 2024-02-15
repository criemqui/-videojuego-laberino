# -videojuego-laberinto

# Laberinto

Este proyecto implementa un juego de laberinto en Python utilizando programación orientada a objetos. El juego permite al jugador moverse por un laberinto representado por un mapa y alcanzar la salida.

## Funcionalidades

- El jugador puede moverse hacia arriba (W), abajo (S) izquierda (A) o derecha (D) en el laberinto.
- El juego termina cuando el jugador alcanza la salida del laberinto.
- El juego utiliza archivos de texto para cargar laberintos aleatorios desde una carpeta.

## Instrucciones de Ejecución

1. Clona este repositorio en tu máquina local.
   
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git



## Estructura de Archivos

- `main.py`: El punto de entrada del programa.
- `juego.py`: Contiene la implementación de las clases `Juego` y `JuegoArchivo`.
- `mapa.txt`: Un ejemplo de archivo de mapa utilizado en el juego.
- `carpeta_de_mapas/`: Carpeta que contiene varios archivos de mapas para el juego.


Aquí está el contenido de texto general.

<details>
<summary>Código de Ejemplo</summary>

```python
from juego import JuegoArchivo

# Define las posiciones inicial y final del jugador
posicion_inicial = (1, 1)
posicion_final = (5, 6)

# Crea una instancia del juego con un archivo de mapa aleatorio
juego = JuegoArchivo("carpeta_de_mapas", posicion_inicial, posicion_final)

# Imprime el mapa inicial
juego.imprimir_mapa()

# Itera hasta que el jugador llegue a la salida
while juego.posicion_inicial != juego.posicion_final:
    direccion = input("Introduce una dirección (arriba, abajo, izquierda, derecha): ")
    juego.mover_jugador(direccion)
