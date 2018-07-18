import RPi.GPIO as GPIO
import time

DR = 16
DL = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(DR,GPIO.IN)
GPIO.setup(DL,GPIO.IN)

for i in range(10000):
     print('\nSensor derecha :',GPIO.input(DR))
     print('\nSensor izquier :',GPIO.input(DL))

