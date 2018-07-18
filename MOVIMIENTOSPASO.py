import RPi.GPIO as GPIO
import time
import MOVIMIENTOS
from VARIABLES import *

###################################################################
#####################FUNCIóN AMBOS#################################
###################################################################
def BOTH(velR,numR,velL,numL):
    repetidoR=0
    repetidoL=0
    if (numR>0):
        GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2,GPIO.LOW)
    else:
        numR=-numR
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.HIGH)
    if (numL>0):
         GPIO.output(IN4,GPIO.HIGH)
         GPIO.output(IN3,GPIO.LOW)
    else:
        numL=-numL
        GPIO.output(IN4,GPIO.LOW)
        GPIO.output(IN3,GPIO.HIGH)
    contadorR=0
    contadorL=0
    while ((contadorR<numR)or(contadorL<numL)):
        if (contadorR<numR):
            PWMA.start(velR)
        else:
            GPIO.output(IN1,GPIO.LOW)
            GPIO.output(IN2,GPIO.LOW)
            PWMA.start(0)
        if (contadorL<numL):
            PWMB.start(velL)
        else:
            GPIO.output(IN3,GPIO.LOW)
            GPIO.output(IN4,GPIO.LOW)
            PWMB.start(0)
        if ((GPIO.input(DataMotorR)==1)and(repetidoR==0)):
            contadorR=contadorR+1
            repetidoR=1
            print ('contador derecha = ',contadorR)
        if((GPIO.input(DataMotorL)==1)and(repetidoL==0)):
            contadorL=contadorL+1
            repetidoL=1
            print ('contador izquierda = ',contadorL)    
        if(GPIO.input(DataMotorR)==0):
            repetidoR=0
        if(GPIO.input(DataMotorL)==0):
            repetidoL=0
            
    MOVIMIENTOS.STOP()
#############################################

