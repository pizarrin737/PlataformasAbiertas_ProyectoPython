#!/usr/bin/python3

###########################################################
# AGREGADO
###########################################################
"""Menú"""

# Imports requeridos
import turtle

pen = turtle.Turtle()
pen.hideturtle()

for i in range(2):  # Crea marco para las opciones
    pen.forward(220)
    pen.left(90)
    pen.forward(60)
    pen.left(90)
pen.goto(0, -60)
for i in range(2):
    pen.forward(220)
    pen.left(90)
    pen.forward(60)
    pen.left(90)

pen.penup()  # Escribe opción para iniciar juego
pen.goto(14, 12)
pen.write("START GAME", font=("Courier",  24, "normal"))

pen.penup()  # Escribe opción para salir del juego
pen.goto(14, -42)
pen.write("EXIT", font=("Courier",  24, "normal"))


def click(x, y):  # Define click para cualquier punto dentro de marcos
    if x > 0 and x < 220 and y > 0 and y < 60:
        print("Bien START")  # Aquí iría el código del juego
    elif x > 0 and x < 220 and y > -60 and y < 0:
        print("Bien EXIT")  # Aquí iría el comando para salir
    else:
        click(x, y)  # Hace que no pase nada en caso de click fuera de marcos


turtle.onscreenclick(click, 1)
turtle.listen()
turtle.done()
