#!/usr/bin/python3

import turtle
from random import randint


def alien_move(alien):
    """
    Función de movimiento de los enemigos.
    Se activa constantmente durante el loop principal del juego.

    alien: Objeto.turtle() correspondiente a un enemigo
    """
    y = alien.ycor()  # Coordenada x del alien
    x = alien.xcor()  # Coordenada y del alien

    # Determina la dirección del movimiento del alien.
    # direction = 1: se mueve a la derecha
    # direction = -1: se mueve a la izquierda
    direction = alien.direction

    # Velocidad horizontal del alien
    avance = 0.01

    # Da movimiento al alien una vez está en posición
    alien.setx(x + direction*avance)

    # Se asegura de que el alien este en la parte superior de la pantalla
    if y > 240:
        alien.forward(avance)
        window.update()
        y = alien.ycor()
    # Condición de limite derecho en la pantalla
    elif alien.xcor() >= 230:
        y = alien.ycor()
        alien.goto(230, y-40)  # Baja al alien 40 pixeles en y
        alien.direction = -1  # Cambia la dirección del alien
    # Condición de limite derecho en la pantalla
    elif alien.xcor() <= -230:
        y = alien.ycor()
        alien.goto(-230, y-40)  # Baja al alien 40 pixeles en y
        alien.direction = 1  # Cambia la dirección del alien


if __name__ == "__main__":
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

    # Creación del enemigo
    alien = turtle.Turtle()
    alien.speed(0)
    alien.shape("triangle")
    alien.color("green")
    alien.right(90)
    alien.penup()
    alien.goto(0, 260)  # Posicion inicial al centro y abajo
    alien.direction = 1  # Inicialmente se mueve a la derecha

    # Para que la ventana rastree los inputs del teclado
    window.listen()

    # Asociacion del teclado con el movimiento de la nave

    while True:
        window.update()

        alien_move(alien)

        # Situación de Game Over
        if alien.ycor() < ship.ycor():
            alien.goto(0, 0)  # Cambiar cuando este listo

        # Bases de la colisión alien-proyectil
        if alien.xcor() == 0 and alien.ycor() == 0:
            y = randint(260, 560)
            x = alien.xcor()
            alien.goto(x, y)
