import os
import random
import keyboard

class JuegoLaberinto:
    def __init__(self, carpeta_mapas, pos_inicial, pos_final):
        self.pos_inicial = pos_inicial
        self.pos_final = pos_final

        # Obtener la lista de archivos en la carpeta de mapas
        lista_archivos = os.listdir(carpeta_mapas)

        # Filtrar la lista de archivos para incluir solo archivos de mapa válidos
        archivos_mapa = [archivo for archivo in lista_archivos if archivo.endswith('.txt')]

        # Verificar si hay archivos de mapa en la carpeta
        if not archivos_mapa:
            print("Error: No se encontraron archivos de mapa en la carpeta especificada.")
            return

        # Seleccionar aleatoriamente un archivo de la lista de archivos de mapa
        archivo_mapa = random.choice(archivos_mapa)

        # Construir la ruta completa al archivo del mapa
        ruta_mapa = os.path.join(carpeta_mapas, archivo_mapa)

        # Leer el contenido del archivo del mapa
        with open(ruta_mapa, 'r') as file:
            self.mapa = [list(linea.strip()) for linea in file]


    def limpiar_y_mostrar_matriz(self, px, py):
        # Limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')

         # Verificar los límites del mapa y las coordenadas del jugador
        print("Tamaño del mapa:", len(self.mapa), "x", len(self.mapa[0]))
        print("Posición del jugador (x, y):", px, py)

        # Copiar el mapa para no modificar el original
        mapa_mostrar = [fila[:] for fila in self.mapa]

        # Colocar al jugador en el mapa
        if 0 <= py < len(self.mapa) and 0 <= px < len(self.mapa[0]):
            mapa_mostrar[py][px] = 'P'
        else:
         print("Error: Las coordenadas del jugador están fuera del rango del mapa.")

        # Mostrar el mapa
        for fila in mapa_mostrar:
            print(''.join(fila))

    def main_loop(self):
        # Coordenadas iniciales del jugador
        px, py = self.pos_inicial

        # Mensaje de bienvenida
        print("¡Bienvenido al laberinto!")
        print("Instrucciones: Utiliza las teclas 'W', 'A', 'S', 'D' para moverte y 'Q' para salir.")

        # Solicitar al usuario que ingrese su nombre
        nombre_jugador = input("Por favor, ingresa tu nombre: ")

        # Mensaje de bienvenida con el nombre del jugador
        print(f"\n¡Hola, {nombre_jugador}! Aquí está el laberinto para que lo explores:\n")

        # Bucle principal del juego
        while True:
            # Limpiar y mostrar el mapa
            self.limpiar_y_mostrar_matriz(px, py)

            # Leer la entrada del usuario
            movimiento = None
            while movimiento not in ['w', 'a', 's', 'd', 'q']:
                try:
                    if keyboard.is_pressed('w'):
                        movimiento = 'w'
                    elif keyboard.is_pressed('a'):
                        movimiento = 'a'
                    elif keyboard.is_pressed('s'):
                        movimiento = 's'
                    elif keyboard.is_pressed('d'):
                        movimiento = 'd'
                    elif keyboard.is_pressed('q'):
                        print("Has salido del juego.")
                        return
                except:
                    pass

            # Actualizar la posición del jugador según la entrada del usuario
            if movimiento == 'w' and py > 0 and self.mapa[py - 1][px] != '#':
                py -= 1
            elif movimiento == 's' and py < len(self.mapa) - 1 and self.mapa[py + 1][px] != '#':
                py += 1
            elif movimiento == 'a' and px > 0 and self.mapa[py][px - 1] != '#':
                px -= 1
            elif movimiento == 'd' and px < len(self.mapa[0]) - 1 and self.mapa[py][px + 1] != '#':
                px += 1

            # Verificar si el jugador llegó a la salida
            if (px, py) == self.pos_final:
                # Limpiar y mostrar el mapa por última vez
                self.limpiar_y_mostrar_matriz(px, py)
                print("\n¡Felicidades, has terminado el laberinto!")
                break



# Nuevo mapa proporcionado
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

# Ruta de la carpeta que contiene los archivos de mapas
carpeta_mapas = os.path.join(os.path.expanduser("~"), "Desktop", "carpeta_mapas")

# Imprime la ruta de la carpeta de mapas
print("Ruta de la carpeta de mapas:", carpeta_mapas)

# Posiciones inicial y final
pos_inicial = (1, 2)
pos_final = (19, 20)

# Crear una instancia del juego
juego = JuegoLaberinto(carpeta_mapas, pos_inicial, pos_final)

# Iniciar el bucle principal del juego
juego.main_loop()
