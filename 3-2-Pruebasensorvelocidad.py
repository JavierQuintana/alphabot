import RPi.GPIO as GPIO

DataMotorR = 7
DataMotorL = 8

GPIO.setmode(GPIO.BCM)

GPIO.setup(DataMotorR,GPIO.IN)
GPIO.setup(DataMotorL,GPIO.IN)


for i in range(100000):
    print('\nMotor derecha   :',GPIO.input(DataMotorR))
    print('\nMotor izquierda :',GPIO.input(DataMotorL))