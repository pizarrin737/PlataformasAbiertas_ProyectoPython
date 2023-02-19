#!/usr/bin/python3
#####################################################################
# AGREGADO con la opción 1
#####################################################################
# Imports
import turtle

""" OPCIÓN 1 Scores """

score = 0  # Variables, hacerlas global dependiendo donde se pongan
high_score = 0

puntaje = turtle.Turtle()  # Parte visual
puntaje.speed(0)  # Probar otros valores para crear animación
puntaje.color("white")  # Depende de color e pantalla final
puntaje.penup()  # Oculta lápiz, podría quitarse para animación
puntaje.hideturtle()
puntaje.goto(0, 450)  # Ver donde ponerlo sin que moleste visualmente
puntaje.write("Score: 0        HighScore: 0",
              align="center", font=("Courier",  24, "normal"))

score += 100  # Colocar en la parte de colisión bala-alien
if score >= high_score:
    high_score = score
puntaje.clear()
puntaje.write("Score: {}        HighScore: {}".format(score, high_score),
              align="center", font=("Courier",  24, "normal"))

score = 0  # Colocar en la parte donde el usuario pierde (GameOver)
puntaje.write("Score: {}        HighScore: {}".format(score, high_score),
              align="center", font=("Courier",  24, "normal"))


""" OPCIÓN 2 Scores """

registro = open("global_high_score.txt", "r")
score = registro.readline().rstrip()
new_high_score = int(score)
registro.close()

score = 0
high_score = new_high_score

puntaje = turtle.Turtle()
puntaje.speed(0)
puntaje.color("white")
puntaje.penup()
puntaje.hideturtle()
puntaje.goto(0, 450)
puntaje.write("Score: 0        HighScore: {}".format(high_score),
              align="center", font=("Courier",  24, "normal"))
score += 100
if score >= high_score:
    high_score = score
    registro = open("global_high_score.txt", "w")
    registro.write(high_score)
    registro.close()
puntaje.clear()
puntaje.write("Score: {}        HighScore: {}".format(score, high_score),
              align="center", font=("Courier",  24, "normal"))
score = 0
puntaje.write("Score: {}        HighScore: {}".format(score, high_score),
              align="center", font=("Courier",  24, "normal"))
