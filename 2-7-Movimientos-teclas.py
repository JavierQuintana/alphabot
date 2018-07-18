import RPi.GPIO as GPIO
import time

import MOVIMIENTOS

print ('TECLAS ¡en minúscula!:\nPARAR = tecla ESPACIO\nADELANTE=FORDWARD = f\nATRAS=BACKWARD = b\nDERECHA=RIGHT = r\nIZQUIERDA=LEFT = l')
tecla='x' 
while tecla!=' ':
    tecla = input('\nPresiona una tecla y después enter : ')
    if tecla != ' ':
        print ('\nHas presionado ', tecla)
        if tecla=='f':
            print ('\nadelante')
            MOVIMIENTOS.FORDWARD(30)
        if tecla=='b':
            print ('\natrás')
            MOVIMIENTOS.BACKWARD(30)
        if tecla=='r':
            print ('\nderecha')
            MOVIMIENTOS.RIGHT(30)
        if tecla=='l':
            print ('\nizquierda')
            MOVIMIENTOS.LEFT(30)

    else:
        print ('\nFin, has apretado STOP')
        MOVIMIENTOS.STOP()
        