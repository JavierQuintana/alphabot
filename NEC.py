import RPi.GPIO as GPIO
import time
from VARIABLES import *

def getkey():
    if GPIO.input(IR) == 0:
        count = 0
        while GPIO.input(IR) == 0 and count < 200:  #9ms
            count += 1
            time.sleep(0.00006)

        count = 0
        while GPIO.input(IR) == 1 and count < 80:  #4.5ms
            count += 1
            time.sleep(0.00006)

        idx = 0
        cnt = 0
        data = [0,0,0,0]
        for i in range(0,32):
            count = 0
            while GPIO.input(IR) == 0 and count < 15:    #0.56ms
                count += 1
                time.sleep(0.00006)

            count = 0
            while GPIO.input(IR) == 1 and count < 40:   #0: 0.56mx
                count += 1                               #1: 1.69ms
                time.sleep(0.00006)

            if count > 8:
                data[idx] |= 1<<cnt
            if cnt == 7:
                cnt = 0
                idx += 1
            else:
                cnt += 1
#        print (data)
        if data[0]+data[1] == 0xFF and data[2]+data[3] == 0xFF:  #check
            return data[2]

        if data[0] == 255 and data[1] == 255 and data[2] == 15 and data[3] == 255:
            return "repeat"