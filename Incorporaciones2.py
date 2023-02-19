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
        avance = 0.2  # Velocidad del proyectil
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
    avance = 0.08

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
    global avaiable, score, high_score

    # Delimitación del hitbox del enemigo (20x20 pixeles actualemnte)
    if (proyectile.xcor() >= alien.xcor()-10  # limite izquierdo
            and
            proyectile.xcor() <= alien.xcor()+10  # limite derecho
            and
            proyectile.ycor() >= alien.ycor()-10  # Limite inferior
            and proyectile.ycor() <= alien.ycor()+10):  # Limite superior

        # Cuando un enemigo es golpeado este se mueve arriba de la ventana
        x = randint(-230, 230)  # Nueva coordenada x (dentro de ventana)
        alien.goto(x, 260)  # Nueva posición del enemigo
        avaiable = True  # El proyectil vuelve a estar disponible
        proyectile.goto(0, -300)  # Proyectil enviado bajo la ventana
        proyectile.hideturtle()  # Se esconde el proyectil

        # Actualiza el marcador del jugador
        score += 100  # Colocar en la parte de colisión bala-alien
        if score >= high_score:
            high_score = score
        puntaje.clear()
        puntaje.write("Score: {}        HighScore: {}".format(score, high_score),
                    align="center", font=("Courier",  24, "normal"))


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
    window.bgcolor("black")
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

    # Creación de los enemigos

    # Enemigo 1
    x1 = randint(-230, 230)  # Coordenada x inicial aleatoria
    alien1 = turtle.Turtle()
    alien1.speed(0)
    alien1.shape("triangle")
    alien1.color("green")
    alien1.right(90)
    alien1.penup()
    alien1.goto(x1, 260)  # Posicion inicial
    alien1.direction = 1  # Inicialmente se mueve a la derecha

    # Enemigo 2
    x2 = randint(-230, 230)  # Coordenada x inicial aleatoria
    alien2 = turtle.Turtle()
    alien2.speed(0)
    alien2.shape("triangle")
    alien2.color("green")
    alien2.right(90)
    alien2.penup()
    alien2.goto(x2, 260)  # Posicion inicial al centro y abajo
    alien2.direction = -1  # Inicialmente se mueve a la izquierda

    # Enemigo 3
    x3 = randint(-230, 230)  # Coordenada x inicial aleatoria
    alien3 = turtle.Turtle()
    alien3.speed(0)
    alien3.shape("triangle")
    alien3.color("green")
    alien3.right(90)
    alien3.penup()
    alien3.goto(x3, 260)  # Posicion inicial
    alien3.direction = 1  # Inicialmente se mueve a la derecha

    # Enemigo 4
    x4 = randint(-230, 230)  # Coordenada x inicial aleatoria
    alien4 = turtle.Turtle()
    alien4.speed(0)
    alien4.shape("triangle")
    alien4.color("green")
    alien4.right(90)
    alien4.penup()
    alien4.goto(x4, 260)  # Posicion inicial al centro y abajo
    alien4.direction = -1  # Inicialmente se mueve a la izquierda

    # Enemigo 5
    x5 = randint(-230, 230)  # Coordenada x inicial aleatoria
    alien5 = turtle.Turtle()
    alien5.speed(0)
    alien5.shape("triangle")
    alien5.color("green")
    alien5.right(90)
    alien5.penup()
    alien5.goto(x5, 260)  # Posicion inicial
    alien5.direction = 1  # Inicialmente se mueve a la derecha

    # Enemigo 6
    x6 = randint(-230, 230)  # Coordenada x inicial aleatoria
    alien6 = turtle.Turtle()
    alien6.speed(0)
    alien6.shape("triangle")
    alien6.color("green")
    alien6.right(90)
    alien6.penup()
    alien6.goto(x6, 260)  # Posicion inicial al centro y abajo
    alien6.direction = -1  # Inicialmente se mueve a la izquierda

    # Enemigo 7
    x7 = randint(-230, 230)  # Coordenada x inicial aleatoria
    alien7 = turtle.Turtle()
    alien7.speed(0)
    alien7.shape("triangle")
    alien7.color("green")
    alien7.right(90)
    alien7.penup()
    alien7.goto(x7, 260)  # Posicion inicial
    alien7.direction = 1  # Inicialmente se mueve a la derecha

    # Enemigo 8
    x8 = randint(-230, 230)  # Coordenada x inicial aleatoria
    alien8 = turtle.Turtle()
    alien8.speed(0)
    alien8.shape("triangle")
    alien8.color("green")
    alien8.right(90)
    alien8.penup()
    alien8.goto(x8, 260)  # Posicion inicial al centro y abajo
    alien8.direction = -1  # Inicialmente se mueve a la izquierda

    # Para que la ventana rastree los inputs del teclado
    window.listen()

    # Asociacion del teclado con el movimiento de la nave
    window.onkeypress(ship_right, "Right")  # Derecha
    window.onkeypress(ship_left, "Left")  # Izquierda
    window.onkeypress(weapon_in_wait, "space")  # Disparo

    # Variable que indica si el jugador perdio o no
    GameOver = False  # El jugador no inicia perdiendo

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
    puntaje.write("Score: 0        HighScore: 0",
                align="center", font=("Courier",  24, "normal"))

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
