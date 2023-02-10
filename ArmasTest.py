#!/usr/bin/python3

import turtle


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
        avance = 0.1  # Velocidad del proyectil
        proyectile.showturtle()  # Vuelve visible el proyectil
        proyectile.forward(avance)

        # Se activa cuando el proyectil está arriba en la pantalla
        if proyectile.ycor() >= 250:
            proyectile.hideturtle()  # Vuelve a ocultar el proyectil
            avaiable = True  # Vuelve a estar disponible
            proyectile.goto(0, -300)  # Mueve el proyectil abajo


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

    # Para que la ventana rastree los inputs del teclado
    window.listen()
    window.onkeypress(weapon_in_wait, "space")

    # Asociacion del teclado con el movimiento de la nave

    while True:
        # Refresca la ventana
        window.update()

        # Anima el proyectil
        weapon_in_use()
