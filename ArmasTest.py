#!/usr/bin/python3

import turtle


def ship_weapons():
    """
    Funcion para para que la nave se mueva a la izquierda.
    Actualmente se activa con la flecha izquierda.
    """
    # Creación de la nave del usuario
    x = ship.xcor()
    y = ship.ycor() + 10
    proyectile = turtle.Turtle()
    proyectile.speed(0)
    proyectile.shape("triangle")
    proyectile.color("white")
    proyectile.left(90)
    proyectile.penup()
    proyectile.goto(x, y)
    avance = 0.05
    while y < 250:
        proyectile.forward(avance)
        window.update()
        y = proyectile.ycor()
    proyectile.reset()


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

    # Para que la ventana rastree los inputs del teclado
    window.listen()

    # Asociacion del teclado con el movimiento de la nave
    window.onkeypress(ship_weapons, "space")

    while True:
        window.update()
