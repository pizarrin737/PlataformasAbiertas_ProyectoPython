#!/usr/bin/python3

import turtle


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


def ship_weapons():
    """
    Función para que el proyectil sea disparado por la nave.
    Actualmente se activa con la barra espaciadora.
    """
    # Variable GLOBAL necesaria para trackear el estado del proyectil
    global avaiable

    # Solo dispara si el proyectil está disponible
    if avaiable is True:
        # NOTA: El track se mueve dentro de la fución para corregir error
        # de posición a la hora del disparo.
        proyectile.goto(ship.xcor(),
                        ship.ycor()+10)  # Regresa a la punta de la nave
        y = proyectile.ycor()
        avance = 0.05  # Velocidad del proyectil
        proyectile.showturtle()  # Vuelve visible el proyectil (Ha disparado)
        while y <= 250:  # Avanza hasta llegar arriba en la pantalla
            proyectile.forward(avance)
            window.update()
            y = proyectile.ycor()
            # NOTA: Recordar posición según lo que se desee
            # 1-dentro del while: 1 disparo
            # 2-fuera del while: multiples disparos
            avaiable = False  # Evita otro disparo cuando ya hay uno activo


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

    # Asociacion del teclado con el movimiento de la nave
    window.onkeypress(ship_right, "Right")  # Derecha
    window.onkeypress(ship_left, "Left")  # Izquierda
    window.onkeypress(ship_weapons, "space")  # Disparo

    while True:
        window.update()

        # Condición de disponibilidad del proyectil
        # Se activa una vez llega arriba en la pantalla
        if proyectile.ycor() >= 250:
            # NOTA: El track del proyectil se traslado a la función
            # ship_weapons() para corregir error de posición
            proyectile.hideturtle()  # Vuelve a ocultar el proyectil
            avaiable = True  # Vuelve a estar disponible
