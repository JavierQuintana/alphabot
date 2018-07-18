import RPi.GPIO as GPIO
import time

from VARIABLES import *

#######################################################
#función de manipulación de bits
#ver https://repl.it/@javierquintana/ObtenerBitEntero
#######################################################
def SACADIRECCION(x,n):
  if (x & (1<<n)):
    GPIO.output(Address,GPIO.HIGH)
  else:
    GPIO.output(Address,GPIO.LOW)

######################################################
#función de obtener lectura del sensor siguelíneas
#cual = el número del siguelíneas a leer 0-4
######################################################
def SENSORLINEA(cual):
  #activo el chip
  GPIO.output(CS,GPIO.LOW)
  for i in range(4):
    #Pongo en Address el bit de cual empezando por MSB 
    SACADIRECCION(cual,3-i)
    #Flanco de subida de Clock para que lo lea
    GPIO.output(Clock,GPIO.LOW)  
    GPIO.output(Clock,GPIO.HIGH)
  #ahora 6 pulsos perdidos
  for i in range(6):
    GPIO.output(Clock,GPIO.LOW)  
    GPIO.output(Clock,GPIO.HIGH)
  #vamos a darle un tiempo para que calcue la convesión A/D
  #A/D Conversion Interval =
  time.sleep(0.001)
  #leemos el número
  #formula valor = sumatorio (potenciasde2 * bit leido)
  #potenciasde2 = 2 elevado al peso del bit
  #el peso del primer bit es MSB luego 9 y acaba en 0 o LSB
  valor=0
  for i in range (10):
    GPIO.output(Clock,GPIO.LOW)  
    GPIO.output(Clock,GPIO.HIGH)
    valor=valor+GPIO.input(DataOut)*(2**(9-i))
  #desactivamos el chip
  GPIO.output(CS,GPIO.HIGH)
  return valor
    