#juego de laberinto 

#importacion de modulos.

import turtle, math

#configuracion de la ventana.
ventana = turtle.Screen()
ventana.bgcolor("black")
ventana.title("Laberinto")
ventana.setup(700, 700)

#crear una clase "Pen" para dibujar las paredes del laberinto
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
     

#esta parte representa el jugador
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)
        self.gold = 0

        #funciones para el movimiento del player
    def arriba(self):
        #Revisar si el lugar al quenos vamos a mover esta ocupado por una pared.
        siguientePasoX = player.xcor()
        siguientePasoY = player.ycor() + 24

        #revisamos si ese espacio tiene una pared.
        if (siguientePasoX, siguientePasoY) not in paredes:
            self.goto(self.xcor(), self.ycor() + 24)

    def abajo(self):
        #revisar si el lugar al que nos vamos a mover esta ocupado por una pared.
        siguientePasoX = player.xcor() 
        siguientePasoY = player.ycor() - 24

        #revisamos si ese espacio tiene una pared.
        if (siguientePasoX, siguientePasoY) not in paredes:
            self.goto(self.xcor(), self.ycor() - 24)

    def izquierda(self):
        #revisar si el lugar al que nos vamos a mover esta ocupado por una pared.
        siguientePasoX = player.xcor() - 24
        siguientePasoY = player.ycor()

        #revisamos si ese espacio tiene pared
        if (siguientePasoX, siguientePasoY) not in paredes:
            self.goto(self.xcor() - 24, self.ycor())

    def derecha(self):
        #resisar si el lugar que nos vamos a mover esta ocupado por una pared.
        siguientePasoX = player.xcor() + 24
        siguientePasoY = player.ycor() 

        #resivamos si ese espacio tiene pared
        if (siguientePasoX, siguientePasoY) not in paredes:
            self.goto(self.xcor() + 24, self.ycor())

#lista de niveles
niveles = ['']

#Primer nivel
NIVEL1 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXX',
    'XPX   X   X       X   X X',
    'X X XXXXX X XXXXXXX X X X',
    'X     X   X         X   X',
    'X XXXXXXX   XXXXXXX   XXX',
    'X   XXXXXXX XXXXXXXX XXXX',
    'XXX       X       X    XX',
    'XXXXXX..XXXXXXX.......XXX',
    'XXXXXX.X....XXXXXXXXXXXXX',
    'XXXX...X.XXXXXXXXX...XXXX',
    'XXX...XX......XXXXXXXXXXX',
    'XXXX....XXXX....XXXXXXXXX',
    'XXXXXX.............XXXXXX',
    'XXXXXXXXXX...XXXXXXXXXXXX',
    'XXXXX................XXXX',
    'XXXXXX..............XXXXX',
    'XXXXXXXX....xxx....XXXXXX',
    'XXXXX...XXXXXXXXXXXXXXXXX',
    'XXXXXXXX......XXXXXXXXXXX',
    'XXX..XXXXXXX....XXXXXXXXX',
    'XXXXXXX....XXXXX...XXXXXX',
    'XXX....XXXXXXXXX..XXXXXXX',
    'XXXXXX........XXXXXXXXXXX',
    'XXX.......XXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXX',
]

#agregar el laberinto a la lista
niveles.append(NIVEL1)


#funciones del laberinto
def configurarLaberinto(nivel):
    for y in range(len(nivel)):
        for x in range(len(nivel[y])):
            #obtener los caracteres en cada coordenada (x,y)
            caracter = nivel[y][x]
            #calcular las coordenada (x,y) de la pantalla
            screenX = -288 + (x * 24)
            screenY = 288 - (y * 24)

            #REVISAMOS SI EL CARACTER ES UNA X, SI ASI DIBUJAREMOS UNA PARED
            if caracter == "X":
                pen.goto(screenX, screenY)
                pen.stamp()
            
                #agrefar las coordenadas a la lista.
                paredes.append((screenX, screenY))

            #EN CASO QUE EL CARACTER SEA UNA LETRA P, REPRESENTA EL JUGAROR
            if caracter == "P":
                player.goto(screenX, screenY)

#crear las instancias de clase.           
pen = Pen()
player = Player()

paredes = []

#configurar el nivel.
configurarLaberinto(niveles[1])

#movimiento del jugador del teclado
turtle.listen()
turtle.onkey(player.arriba, 'Up')
turtle.onkey(player.abajo, 'Down')
turtle.onkey(player.izquierda, 'Left')
turtle.onkey(player.derecha, 'Right')

#agarramos las actualizaciones de la ventana
ventana.tracer(0)

#ciclo del juego
while True:
#actualizamos la pantalla
    ventana.update()