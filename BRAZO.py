import RPi.GPIO as GPIO
import time

from VARIABLES import *

servox = GPIO.PWM(SERVOEJEX,40)
servoz = GPIO.PWM(SERVOEJEZ,40)
servox.start(0)
servoz.start(0)

def ANGULO(angle,x):
    if (x):
        servox.ChangeDutyCycle(2.5 + 10.0 * angle / 180)
    else:
        servoz.ChangeDutyCycle(2.5 + 10.0 * angle / 180)

