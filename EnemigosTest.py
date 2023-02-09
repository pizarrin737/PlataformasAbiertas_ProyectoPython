#!/usr/bin/python3

import turtle
# import random


def alien_move_x(alien):
    # Pasar a funcion de mov vertical
    # y = alien.ycor()
    x = alien.xcor()
    direction = alien.direction
    avance = 0.01
    # Pasar a funcion de mov vertical
    # ----while y > 240:
    # ----alien.forward(avance)
    # ----window.update()
    # ----y = alien.ycor()
    alien.setx(x + direction*avance)


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
    alien.goto(0, 250)  # Posicion inicial al centro y abajo
    alien.direction = 1

    # Para que la ventana rastree los inputs del teclado
    window.listen()

    # Asociacion del teclado con el movimiento de la nave

    while True:
        window.update()

        alien_move_x(alien)

        # Pasar a funcion de mov vertical
        if alien.xcor() >= 230:
            y = alien.ycor()
            alien.goto(230, y-40)
            alien.direction = -1
        elif alien.xcor() <= -230:
            y = alien.ycor()
            alien.goto(-230, y-40)
            alien.direction = 1
