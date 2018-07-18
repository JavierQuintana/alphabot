import RPi.GPIO as GPIO
import time

import TLC1543
 
while True:
    for i in range(5):
        x=TLC1543.SENSORLINEA(i)
        print (" Sensor",i,"= ",x,end="")
    print(" ");
    time.sleep(0.5)
    