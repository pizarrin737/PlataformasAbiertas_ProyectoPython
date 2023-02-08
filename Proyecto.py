#!/usr/bin/python3

import turtle
import time


def ship_stop():
    """
    Funcion para detener el movimiento de la nave.
    Actualmente no se usa.
    """
    ship.move = "stop"


def ship_right():
    """
    Funcion para para cambiar el estado de la nave a moverse a la dereha.
    Actualmente se activa con la flecha derecha.
    """
    ship.move = "right"


def ship_left():
    """
    Funcion para para cambiar el estado de la nave a moverse a la izquierda.
    Actualmente se activa con la flecha izquierda.
    """
    ship.move = "left"


def ship_move(ship):
    """"
    Funcion para mover la nave.
    Actualiza las coordenadas de la nave según su estado.
    """
    x = ship.xcor()  # Coordenada x actual
    if ship.move == "right":
        ship.setx(x + 2.5)  # Mueve la nave 2.5 pixeles a la derecha
    elif ship.move == "left":
        ship.setx(x - 2.5)  # Mueve la nave 2.5 pixeles a la izquierda


if __name__ == "__main__":
    # Retardo para relentizar las animaciones
    delay = 0.01

    # Creación de la ventana del juego
    window = turtle.Screen()
    window.title("Alien Invaders")
    window.setup(width=500, height=500)  # Unidades en pixeles
    window._bgcolor("black")
    window.tracer(0)

    # Creación de la nave del usuario
    ship = turtle.Turtle()
    ship.speed(0)
    ship.shape("arrow")
    ship.color("white")
    ship.left(90)
    ship.penup()
    ship.goto(0, -240)  # Posicion inicial al centro y abajo
    ship.move = "stop"  # Estado de movimiento inicial

    # Para que la ventana rastrre los inputs del teclado
    window.listen()

    # Asociacion del teclado con el movimiento de la nave
    window.onkeypress(ship_right, "Right")
    window.onkeypress(ship_left, "Left")
    window.onkeyrelease(ship_stop, "Right")
    window.onkeyrelease(ship_stop, "Left")

    while True:
        window.update()
        ship_move(ship)
        time.sleep(delay)
