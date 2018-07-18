import RPi.GPIO as GPIO
import time

from VARIABLES import *

import BRAZO

angulox=90
anguloz=90
incremento=20
print("Teclas 8 y 2 SERVOX\n Teclas 4 y 6 SERVOZ")
while True:
    BRAZO.ANGULO(angulox,1)
    BRAZO.ANGULO(anguloz,0)
    tecla=input("Mueve el brazo : ")
    if (tecla=="8"):
        angulox=angulox-incremento
    if (tecla=="2"):
        angulox=angulox+incremento
    if (tecla=="4"):
        anguloz=anguloz+incremento
    if (tecla=="6"):
        anguloz=anguloz-incremento
    
        
    
