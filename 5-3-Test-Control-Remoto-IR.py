import RPi.GPIO as GPIO
import time

from VARIABLES import *

import MOVIMIENTOS
import MOVIMIENTOSPASO
import NEC

while True:
    key=NEC.getkey()
    if (key != None):
        print (key)
        