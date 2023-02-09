#!/usr/bin/python3

import turtle


def ship_weapons():
    """
    Función para que el proyectil sea disparado por la nave.
    Actualmente se activa con la barra espaciadora.
    """
    # Variable GLOBAL necesaria para trackear el estado del proyectil
    global avaiable

    # Solo dispara si el proyectil está disponible
    if avaiable is True:
        y = proyectile.ycor()
        avance = 0.05  # Velocidad del proyectil
        while y <= 250:  # Avanza hasta llegar arriba en la pantalla
            proyectile.forward(avance)
            window.update()
            y = proyectile.ycor()
        avaiable = False  # Evita otro disparo cuando ya hay un disparo activo


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

    # Creación del proyectil que dispara el usuario
    # Fue necesario sacarlo de la función ya que sino el loop principal crashea
    proyectile = turtle.Turtle()
    proyectile.speed(0)
    proyectile.shape("circle")
    proyectile.color("red")
    proyectile.left(90)
    proyectile.penup()
    proyectile.goto(ship.xcor(),
                    ship.ycor()+10)  # Ubicado en la punta de la nave
    avaiable = True  # Disponibilidad del proyectil. Disponible al inicio

    # Para que la ventana rastree los inputs del teclado
    window.listen()

    # Asociacion del teclado con el movimiento de la nave
    window.onkeypress(ship_weapons, "space")

    while True:
        window.update()

        # Condición de disponibilidad del proyectil
        # Se activa una vez llega arriba en la pantalla
        if proyectile.ycor() >= 250:
            proyectile.goto(ship.xcor(),
                            ship.ycor()+10)  # Regresa a la punta de la nave
            avaiable = True  # Vuelve a estar disponible
