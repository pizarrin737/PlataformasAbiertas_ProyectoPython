#!/usr/bin/python3


"""Función para sonido de fondo, balas y explosión por colisión"""

########################################################
# Agregado
# Imports requeridos
import platform
import turtle
import os

# Función


def sounds(sound_file, time=0):  # time = 0 inmediatos
    # sounds("BOOM.wav") para colisión bala-alien y alien-nave
    # sounds("BULLET.wav") para bala al ser disparada
    # sounds("BACKGROUND.wav", 16) para sonido de fondo al iniciar juego
    # Importante que archivos de sonido estén en la misma carpeta
    # TODOS LOS SONIDOS SON DE LIBRE USO. https://orangefreesounds.com/
    if platform.system() == "Linux":
        os.system("aplay -q {}&".format(sound_file))
    # & para no pausar el juego al reproducirse sonido
    elif time > 0:
        # time(s): tiempo que dura el sonido.
        # t(ms): tiempo en volver a reproducirse.
        turtle.ontimer(lambda: sounds(sound_file, time), t=int(time*1000))
