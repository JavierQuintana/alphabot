import RPi.GPIO as GPIO
import time
from VARIABLES import *
import MOVIMIENTOS
import MOVIMIENTOSPASO

while True:
    sensorR= not (GPIO.input(DR))
    sensorL= not (GPIO.input(DR))
    if not(sensorR and sensorL):
         MOVIMIENTOS.FORDWARD(50)
    if (sensorR and sensorL):
        MOVIMIENTOSPASO.BOTH(50,-10,50,-10)
    if (sensorR and not(sensorL)):
        MOVIMIENTOSPASO.BOTH(50,-5,50,-5)
        MOVIMIENTOSPASO.BOTH(40,-5,40,5)
    if (not(sensorR) and (sensorL)):
        MOVIMIENTOSPASO.BOTH(50,-5,50,-5)
        MOVIMIENTOSPASO.BOTH(40,5,40,-5)    
    
    
    
