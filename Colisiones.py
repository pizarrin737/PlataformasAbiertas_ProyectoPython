#!/usr/bin/python3

import turtle
from random import randint


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


def colisiones(alien, proyectile):
    """
    Función de rastreo de colisiones enemigo-proyectil.
    Se activa constantmente durante el loop principal del juego.

    alien: Objeto.turtle() correspondiente a un enemigo.
    alien: Objeto.turtle() correspondiente a el proyectil del usuario.
    """

    # Variable GLOBAL necesaria para trackear el estado del proyectil
    global avaiable

    # Delimitación del hitbox del enemigo (20x20 pixeles actualemnte)
    if (proyectile.xcor() >= alien.xcor()-10  # limite izquierdo
            and
            proyectile.xcor() <= alien.xcor()+10  # limite derecho
            and
            proyectile.ycor() >= alien.ycor()-10  # Limite inferior
            and proyectile.ycor() <= alien.ycor()+10):  # Limite superior

        # Cuando un enemigo es golpeado este se mueve arriba de la ventana
        y = randint(260, 360)  # Nueva coordenada y (furera de ventana)
        x = randint(-230, 230)  # Nueva coordenada x (dentro de ventana)
        alien.goto(x, y)  # Nueva posición del enemigo
        avaiable = True  # El proyectil vuelve a estar disponible
        proyectile.goto(0, -300)  # Proyectil enviado bajo la ventana
        proyectile.hideturtle()  # Se esconde el proyectil


def Game_Over(alien):
    """
    Función de rastreo si un enemigo llega al nivel del jugador.
    Si ocuurre termina la partida.
    Se activa constantmente durante el loop principal del juego.

    alien: Objeto.turtle() correspondiente a un enemigo.
    """

    # Variable GLOBAL necesaria para trackear el estado de la partida
    global GameOver

    # Situación de Game Over
    if alien.ycor() < ship.ycor():
        GameOver = True


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

    # Creación del enemigo
    alien1 = turtle.Turtle()
    alien1.speed(0)
    alien1.shape("triangle")
    alien1.color("green")
    alien1.right(90)
    alien1.penup()
    alien1.goto(0, 260)  # Posicion inicial al centro y abajo
    alien1.direction = 1  # Inicialmente se mueve a la derecha

    # Para que la ventana rastree los inputs del teclado
    window.listen()

    # Asociacion del teclado con el movimiento de la nave
    window.onkeypress(ship_right, "Right")  # Derecha
    window.onkeypress(ship_left, "Left")  # Izquierda
    window.onkeypress(weapon_in_wait, "space")  # Disparo

    # Variable que indica si el jugador perdio o no
    GameOver = False  # El jugador no inicia perdiendo

    while GameOver is False:
        # Refresca la ventana
        window.update()

        # Anima el proyectil
        weapon_in_use()

        # Anima los enemigos
        alien_move(alien1)

        # Colisiones enemigo-proyectil
        colisiones(alien1, proyectile)

        # Verifica si el jugador no ha perdido
        Game_Over(alien1)
