import RPi.GPIO as GPIO
import time

from VARIABLES import *

import BRAZO
import MOVIMIENTOS
import MOVIMIENTOSPASO


velR=30
numR=10
velL=30
numL=10

angulox=90
anguloz=90
incremento=20
print("Teclas 8 y 2 SERVOX\n Teclas 4 y 6 SERVOZ")
print ('TECLAS ¡en minúscula!:\nADELANTE=FORDWARD = f\nATRAS=BACKWARD = b\nDERECHA=RIGHT = r\nIZQUIERDA=LEFT = l')
tecla='x'

print ('Mira la cámara en http://192.168.1.25:8080')

while True:
    BRAZO.ANGULO(angulox,1)
    BRAZO.ANGULO(anguloz,0)
    tecla=input("Mueve el brazo o movimiento: ")
    if (tecla=="8"):
        angulox=angulox-incremento
    if (tecla=="2"):
        angulox=angulox+incremento
    if (tecla=="4"):
        anguloz=anguloz+incremento
    if (tecla=="6"):
        anguloz=anguloz-incremento
    if tecla=='f':
        print ('\nadelante')
        MOVIMIENTOSPASO.BOTH(velR,numR,velL,numL)
    if tecla=='b':
        print ('\natrás')
        MOVIMIENTOSPASO.BOTH(velR,-numR,velL,-numL)
    if tecla=='r':
        print ('\nderecha')
        MOVIMIENTOSPASO.BOTH(velR,-numR,velL,numL)
    if tecla=='l':
        print ('\nizquierda')
        MOVIMIENTOSPASO.BOTH(velR,numR,velL,-numL)
