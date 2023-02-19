#!/usr/bin/python3

"""Game Over"""

# Imports
import turtle

# Poner en colisión nave-alien
window.clear()  # window es el nombre de la pantalla gráfica
final_screen = turtle.Turtle()
final_screen.speed(0)
final_screen.color("black")
final_screen.penup()
final_screen.hideturtle()
final_screen.goto(0, 250)
final_screen.write("GAME OVER", align="center",
                   font=("Courier",  40, "normal"))

# Tamaño letra pendiente a cambios
