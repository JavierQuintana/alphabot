import RPi.GPIO as GPIO
import time

import MOVIMIENTOS
import MOVIMIENTOSPASO

velR=30
numR=10
velL=30
numL=10

print ('TECLAS ¡en minúscula!:\nPARAR = tecla 5\nADELANTE=FORDWARD = 8\nATRAS=BACKWARD = 2\nDERECHA=RIGHT = 4\nIZQUIERDA=LEFT = 6')
tecla='x' 
while tecla!='5':
    tecla = input('\nPresiona una tecla y después enter : ')
    if tecla != '5':
        print ('\nHas presionado ', tecla)
        if tecla=='8':
            print ('\nadelante')
            MOVIMIENTOSPASO.BOTH(velR,numR,velL,numL)
        if tecla=='2':
            print ('\natrás')
            MOVIMIENTOSPASO.BOTH(velR,-numR,velL,-numL)
        if tecla=='6':
            print ('\nderecha')
            MOVIMIENTOSPASO.BOTH(velR,-numR,velL,numL)
        if tecla=='4':
            print ('\nizquierda')
            MOVIMIENTOSPASO.BOTH(velR,numR,velL,-numL)

    else:
        print ('\nFin, has apretado STOP')
        MOVIMIENTOS.STOP()
