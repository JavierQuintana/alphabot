import RPi.GPIO as GPIO

DataMotorR = 7
DataMotorL = 8

GPIO.setmode(GPIO.BCM)

GPIO.setup(DataMotorR,GPIO.IN)
GPIO.setup(DataMotorL,GPIO.IN)

contador=0
repetido=0
num = 100
while (contador<num):
    if((GPIO.input(DataMotorR)==1)and(repetido==0)):
        contador=contador+1
        print('\nContador :',contador)
        repetido=1
    if(GPIO.input(DataMotorR)==0):
        repetido=0