#!/usr/bin/python3
""""
Autores:
Carlos Naranjo Arias (B44870)
Christopher David Vega Cedeño (C18390)
Jose Miguel Pizarro Viales (B86079)

En el presente archivo se incluye el código empleado para cumplir con las
asignaciones dadas en proyecto de Python. De esta forma se elaboro un
juego similar a alien invaders por medio Python.

El juego incluye un menu, un espacio de juego, un avatar para el usuario,
multiples enemigos, una mecanica de disparo, efectos visuales y de sonido,
y una pantalla de Game Over.
"""

import turtle
from random import randint
import os
import platform
import time


class explosion(turtle.Turtle):
    """
    se declara una clase con la cual se crea un objeto tipo turtle
    usando el metodo inicializador, el cual va a tener las caracteristicas
    especificadas, como la forma, que se le da usando el contenedor visual
    .frame en donde se almacena una serie de imagenes que generan el efecto
    visual de explosion
    """

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("1.gif")
        self.frame1 = 0
        self.frame = [
            "1.gif", "2.gif", "3.gif", "4.gif", "5.gif",
            "6.gif", "7.gif", "8.gif", "9.gif", "10.gif", "11.gif", "12.gif",
            "13.gif", "14.gif", "14.gif", "15.gif", "16.gif", "17.gif",
            "18.gif", "19.gif", "20.gif", "21.gif", "22.gif", "23.gif",
            "24.gif", "25.gif"
            ]

    def animacion(self):
        """
        funcion se que recorre el frame con un ciclo y ademas,
        muestra la imagens a una velocidad especificada con el metodo
        ontimer
        """
        if self.frame1 < len(self.frame)-1:
            self.frame1 += 1
        self.shape(self.frame[self.frame1])
        window.ontimer(self.animacion, 18)
        self.clear()


def sounds(sound_file, time=0):  # time = 0 inmediatos
    # sounds("BOOM.wav") para colisión bala-alien y alien-nave
    # sounds("PIUMcut.wav") para bala al ser disparada
    # sounds("BACKGROUND.2.wav", 16) para sonido de fondo al iniciar juego
    # Importante que archivos de sonido estén en la misma carpeta
    if platform.system() == "Linux":
        os.system("aplay -q {}&".format(sound_file))
    # & para no pausar el juego al reproducirse sonido
    elif time > 0:
        # time(s): tiempo que dura el sonido.
        # t(ms): tiempo en volver a reproducirse.
        turtle.ontimer(lambda: sounds(sound_file, time), t=int(time*1000))


def ship_right():
    """
    Funcion para que la nave se mueva a la dereha.
    Actualmente se activa con la flecha derecha.
    """
    x = ship.xcor()  # Coordenada x actual
    if x >= 230:
        ship.setx(230)  # Condicion para no salirse del borde derecho
    else:
        ship.setx(x + 10)  # Mueve la nave 10 pixeles a la derecha


def ship_left():
    """
    Funcion para para que la nave se mueva a la izquierda.
    Actualmente se activa con la flecha izquierda.
    """
    x = ship.xcor()  # Coordenada x actual
    if x <= -230:
        ship.setx(-230)  # Condicion para no salirse del borde izquierdo
    else:
        ship.setx(x - 10)  # Mueve la nave 10 pixeles a la izquierda


def weapon_in_wait():
    """
    Función empleada para iniciar la acción de disparo.
    Si el proyectil está en espera, cuando el usuario dispara,
    la función mueve el proyecil a la punta de la nave y activa
    la señal de disparo.

    Actualmente se activa con la barra espaciadora si avaiable == True.
    """
    # Variable GLOBAL necesaria para trackear el estado del proyectil
    global avaiable

    # Solo dispara si el proyectil está disponible
    if avaiable is True:

        # Sonido del proyectil
        sounds("PIUMcut.wav")

        # Regresa el proyectil a la punta de la nave
        proyectile.goto(ship.xcor(), ship.ycor()+10)

        # Ahora el proyectil no está disponible (Disparo activo)
        avaiable = False

        # NOTA: si avaiable == False, se activa weapon_in_use()


def weapon_in_use():
    """
    Función empleada para animar la acción de disparo.
    Si el proyectil está en uso, la función recibe la señal de
    disparo y mueve el proyectil hacia adelante. Una vez el proyectil
    llega hasta arriba en la pantalla lo mueve por debajo del espacio
    de juego para evitar colisiones indeseadas.

    Se activa solo si avaiable == False (proyectil disparado)
    """
    # Variable GLOBAL necesaria para trackear el estado del proyectil
    global avaiable

    # Inicia la animación de disparo si el proyectil está en uso
    if avaiable is False:
        avance = 0.8  # Velocidad del proyectil
        proyectile.showturtle()  # Vuelve visible el proyectil
        proyectile.forward(avance)

        # Se activa cuando el proyectil está arriba en la pantalla
        if proyectile.ycor() >= 250:
            proyectile.hideturtle()  # Vuelve a ocultar el proyectil
            avaiable = True  # Vuelve a estar disponible
            proyectile.goto(0, -300)  # Mueve el proyectil abajo


def alien_move(alien):
    """
    Función de movimiento de los enemigos.
    Se activa constantmente durante el loop principal del juego.

    alien: Objeto.turtle() correspondiente a un enemigo.
    """
    y = alien.ycor()  # Coordenada x del alien
    x = alien.xcor()  # Coordenada y del alien

    # Determina la dirección del movimiento del alien.
    # direction = 1: se mueve a la derecha
    # direction = -1: se mueve a la izquierda
    direction = alien.direction

    # Velocidad horizontal del alien
    avance = 0.45

    # Da movimiento al alien una vez está en posición
    alien.setx(x + direction*avance)

    # Condición de limite derecho en la pantalla
    if alien.xcor() >= 230:
        y = alien.ycor()
        alien.goto(230, y-40)  # Baja al alien 40 pixeles en y
        alien.direction = -1  # Cambia la dirección del alien

    # Condición de limite derecho en la pantalla
    elif alien.xcor() <= -230:
        y = alien.ycor()
        alien.goto(-230, y-40)  # Baja al alien 40 pixeles en y
        alien.direction = 1  # Cambia la dirección del alien


def colisiones(alien, proyectile):
    """
    Función de rastreo de colisiones enemigo-proyectil.
    Se activa constantmente durante el loop principal del juego.

    alien: Objeto.turtle() correspondiente a un enemigo.
    alien: Objeto.turtle() correspondiente a el proyectil del usuario.
    """

    # Variable GLOBAL avaiable para trackear el estado del proyectil
    # Variable GLOBAL score para trackear la puntuación
    # Variable GLOBAL high_score para trackear la puntuación máxima
    global avaiable, score, high_score

    # Delimitación del hitbox del enemigo (20x20 pixeles actualemnte)
    if (proyectile.xcor() >= alien.xcor()-10  # limite izquierdo
            and
            proyectile.xcor() <= alien.xcor()+10  # limite derecho
            and
            proyectile.ycor() >= alien.ycor()-10  # Limite inferior
            and proyectile.ycor() <= alien.ycor()+10):  # Limite superior

        # Sonido de destrucción del enemigo
        sounds("BOOM.wav")

        explo = explosion()  # se llama la clase para crear la explosion
        explo.goto(alien.xcor(), alien.ycor())  # coloca la explosio en el
        # mismo lugar donde se intersecan el proyectil y el alien
        explo.animacion()  # llama la animacion visual de explosion

        # Cuando un enemigo es golpeado este se mueve arriba de la ventana
        x = randint(-230, 230)  # Nueva coordenada x (dentro de ventana)
        alien.goto(x, 260)  # Nueva posición del enemigo
        avaiable = True  # El proyectil vuelve a estar disponible
        proyectile.goto(0, -300)  # Proyectil enviado bajo la ventana
        proyectile.hideturtle()  # Se esconde el proyectil

        # Actualiza el marcador del jugador
        score += 100
        if score >= high_score:
            high_score = score
        puntaje.clear()
        puntaje.write("Score: {}        HighScore: {}".format(
            score, high_score
            ),
            align="center", font=("Courier",  24, "normal")
            )


def Game_Over(alien):
    """
    Función de rastreo si un enemigo llega al nivel del jugador.
    Si ocuurre termina la partida.
    Se activa constantmente durante el loop principal del juego.

    alien: Objeto.turtle() correspondiente a un enemigo.
    """

    # Variable GLOBAL GameOver para trackear el estado de la partida
    # Variable GLOBAL score para trackear la puntuación
    # Variable GLOBAL high_score para trackear la puntuación máxima
    global GameOver, score, high_score

    # Situación de Game Over
    if alien.ycor() <= ship.ycor()+20:
        GameOver = True
        # Resetea el score para la proxima partida
        score = 0
        puntaje.clear()
        puntaje.write("Score: {}        HighScore: {}".format(
            score, high_score
            ),
            align="center", font=("Courier",  24, "normal")
            )


def click(x, y):
    """
    Función empleada para manejar el menu principal del juego.
    Define un hitbox en el cual el mouse puede tocar los botones

    Actualmente se activa con el click derecho del mouse.
    """

    # Variable GLOBAL para iniciar la partida
    global start

    # Condición para iniciar partida
    if x > -110 and x < 110 and y > 0 and y < 60:
        # Cambia el color de la pantalla
        window.bgcolor("black")

        # Vuelve visibles los objetos
        ship.showturtle()
        alien1.showturtle()
        alien2.showturtle()
        alien3.showturtle()
        alien4.showturtle()
        alien5.showturtle()
        alien6.showturtle()
        alien7.showturtle()
        alien8.showturtle()

        # Condición de inicio de partida
        start = True
    # Condición para cerrar el programa
    elif x > -110 and x < 110 and y > -60 and y < 0:
        start = False
    else:
        click(x, y)  # Hace que no pase nada en caso de click fuera de marcos


def NewGamePlus(alien):
    """
    Función empleada para reacomodar a los enemigos para empezar
    una nueva partida
    """
    x = randint(-230, 230)  # Coordenada x inicial aleatoria
    alien.penup()
    alien.hideturtle()  # Esconde al enemigo
    alien.goto(x, 260)  # Devulve al enemigo arriba en la pantalla
    alien.speed(0)
    alien.shape("turtle")
    alien.color("green")


if __name__ == "__main__":
    """
    Archivo principal del juego Turtle Invsion.

    Controles:
    menu: click derecho del mouse.
    movimiento: flechas izquiera y derecha
    disparo: barra espaciadora
    """

    # Creación de la ventana del juego
    window = turtle.Screen()
    window.title("Turtle Invasion")
    window.setup(width=800, height=800)  # Unidades en pixeles
    window.bgcolor("black")
    window.tracer(0)

    # Se usa para crear los botones del menu
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.color("white")
    pen.pensize(2)
    pen.goto(-110, 60)

    # Delimitación del espacio de juego
    border = turtle.Turtle()
    border.speed(0)
    border.color("white")
    border.penup()
    border.hideturtle()
    border.goto(-250, 270)
    border.pensize(3)
    border.pendown()
    for i in range(2):
        border.forward(500)
        border.right(90)
        border.forward(520)
        border.right(90)

    # Creación de la nave del usuario
    ship = turtle.Turtle()
    ship.hideturtle()
    ship.speed(0)
    ship.shape("arrow")
    ship.color("yellow")
    ship.left(90)
    ship.penup()
    ship.goto(0, -240)  # Posicion inicial al centro y abajo

    # Creación del proyectil que dispara el usuario
    proyectile = turtle.Turtle()
    proyectile.hideturtle()  # Inicialmente oculto (No ha disparado)
    proyectile.speed(0)
    proyectile.shape("circle")
    proyectile.color("red")
    proyectile.turtlesize(0.14, 0.52)
    proyectile.left(90)
    proyectile.penup()
    proyectile.goto(ship.xcor(),
                    ship.ycor()+10)  # Ubicado en la punta de la nave
    avaiable = True  # Disponibilidad del proyectil. Disponible al inicio

    # se importan todas las imagenes que se
    # usan para crear la explosion
    window.addshape("1.gif")
    window.addshape("2.gif")
    window.addshape("3.gif")
    window.addshape("4.gif")
    window.addshape("5.gif")
    window.addshape("6.gif")
    window.addshape("7.gif")
    window.addshape("8.gif")
    window.addshape("9.gif")
    window.addshape("10.gif")
    window.addshape("11.gif")
    window.addshape("12.gif")
    window.addshape("13.gif")
    window.addshape("14.gif")
    window.addshape("15.gif")
    window.addshape("16.gif")
    window.addshape("17.gif")
    window.addshape("18.gif")
    window.addshape("19.gif")
    window.addshape("20.gif")
    window.addshape("21.gif")
    window.addshape("22.gif")
    window.addshape("23.gif")
    window.addshape("24.gif")
    window.addshape("25.gif")

    # Creación de los enemigos

    # Enemigo 1
    alien1 = turtle.Turtle()
    alien1.direction = 1  # Inicialmente se mueve a la derecha
    alien1.right(90)
    NewGamePlus(alien1)

    # Enemigo 2
    alien2 = turtle.Turtle()
    alien2.direction = -1  # Inicialmente se mueve a la izquierda
    alien2.right(90)
    NewGamePlus(alien2)  # Posicion inicial al centro y abajo

    # Enemigo 3
    alien3 = turtle.Turtle()
    alien3.direction = 1  # Inicialmente se mueve a la derecha
    alien3.right(90)
    NewGamePlus(alien3)

    # Enemigo 4
    alien4 = turtle.Turtle()
    alien4.direction = -1  # Inicialmente se mueve a la izquierda
    alien4.right(90)
    NewGamePlus(alien4)  # Posicion inicial al centro y abajo

    # Enemigo 5
    alien5 = turtle.Turtle()
    alien5.direction = 1  # Inicialmente se mueve a la derecha
    alien5.right(90)
    NewGamePlus(alien5)

    # Enemigo 6
    alien6 = turtle.Turtle()
    alien6.direction = -1  # Inicialmente se mueve a la izquierda
    alien6.right(90)
    NewGamePlus(alien6)  # Posicion inicial al centro y abajo

    # Enemigo 7
    alien7 = turtle.Turtle()
    alien7.direction = 1  # Inicialmente se mueve a la derecha
    alien7.right(90)
    NewGamePlus(alien7)

    # Enemigo 8
    alien8 = turtle.Turtle()
    alien8.direction = -1  # Inicialmente se mueve a la izquierda
    alien8.right(90)
    NewGamePlus(alien8)

    # Para que la ventana rastree los inputs del teclado
    window.listen()

    # Asociacion del mouse con el menu
    window.onscreenclick(click, 1)

    # Asociacion del teclado con el movimiento de la nave
    window.onkeypress(ship_right, "Right")  # Derecha
    window.onkeypress(ship_left, "Left")  # Izquierda
    window.onkeypress(weapon_in_wait, "space")  # Disparo

    # Variables que almacenan la puntuación
    score = 0
    high_score = 0

    # Creación del marcador en pantalla
    puntaje = turtle.Turtle()  # Parte visual
    puntaje.speed(0)  # Probar otros valores para crear animación
    puntaje.color("white")  # Depende de color e pantalla final
    puntaje.penup()  # Oculta lápiz, podría quitarse para animación
    puntaje.hideturtle()
    puntaje.goto(0, 300)  # Ver donde ponerlo sin que moleste visualmente
    puntaje.write("Score: {}        HighScore: {}".format(
            score, high_score
            ),
            align="center", font=("Courier",  24, "normal")
            )

    # Titulo de GameOver
    final_screen = turtle.Turtle()
    final_screen.speed(0)
    final_screen.color("red")
    final_screen.penup()
    final_screen.hideturtle()

    # Variable que indica si el jugador perdio o no
    GameOver = False  # El jugador no inicia perdiendo

    # Variable que indica el estado del programa
    start = None  # Inicialmente indefinido

    # Loop principal del programa
    while True:

        # Crea marco para las opciones del menu
        pen.pendown()
        for i in range(2):
            pen.forward(220)
            pen.right(90)
            pen.forward(60)
            pen.right(90)
        pen.goto(-110, 0)
        for i in range(2):
            pen.forward(220)
            pen.right(90)
            pen.forward(60)
            pen.right(90)
        pen.penup()

        # Escribe opción para iniciar juego
        pen.goto(-95, 10)
        pen.write("START GAME", font=("Courier",  24, "normal"))

        # Escribe opción para salir del juego
        pen.goto(-35, -50)
        pen.write("EXIT", font=("Courier",  24, "normal"))
        pen.goto(-110, 60)

        # Permite al usuario decidir que hacer desde el menu
        while start is None:
            window.update()

        pen.clear()

        # Se activa si el usuario decide iniciar una partida
        if start is True:

            # Se usa para agregar sonido de fondo
            # La canción solo suena un vez y no se repite
            """
            sounds("BACKGROUND.2.wav", 145)
            """

            # Delimita lo más que se pueden acrcar los enemigos
            final_screen.goto(-247, -220)
            final_screen.pendown()
            final_screen.forward(494)
            final_screen.penup()
            final_screen.goto(0, 150)

            # Loop principal de juego
            while GameOver is False:

                # Refresca la ventana
                window.update()

                # Anima el proyectil
                weapon_in_use()

                # Anima los enemigos
                alien_move(alien1)
                alien_move(alien2)
                alien_move(alien3)
                alien_move(alien4)
                alien_move(alien5)
                alien_move(alien6)
                alien_move(alien7)
                alien_move(alien8)

                # Colisiones enemigo-proyectil
                colisiones(alien1, proyectile)
                colisiones(alien2, proyectile)
                colisiones(alien3, proyectile)
                colisiones(alien4, proyectile)
                colisiones(alien5, proyectile)
                colisiones(alien6, proyectile)
                colisiones(alien7, proyectile)
                colisiones(alien8, proyectile)

                # Verifica si el jugador no ha perdido
                Game_Over(alien1)
                Game_Over(alien2)
                Game_Over(alien3)
                Game_Over(alien4)
                Game_Over(alien5)
                Game_Over(alien6)
                Game_Over(alien7)
                Game_Over(alien8)

            # Muestra la pantalla de Game Over
            final_screen.write("GAME OVER", align="center",
                               font=("Courier",  40, "normal")
                               )

            window.update()
            time.sleep(2)  # Delay de 2 s
            final_screen.clear()

            NewGamePlus(alien1)
            NewGamePlus(alien2)
            NewGamePlus(alien3)
            NewGamePlus(alien4)
            NewGamePlus(alien5)
            NewGamePlus(alien6)
            NewGamePlus(alien7)
            NewGamePlus(alien8)

            # Esconde a la nave del jugador
            ship.hideturtle()

            # Reseteo de las variables
            start = None  # Cambia el estado del programa a indefinido
            GameOver = False  # Permite al jugador iniciar otra partida

        # Se activa si el usuario decide cerrar el programa
        else:
            break
