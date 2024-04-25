import RPi.GPIO as gpio
from time import sleep
#Variables para pines
DIR = 38;STEP = 40;CW =1;CCW =0

gpio.setmode(gpio.BOARD)
gpio.setup(DIR, gpio.OUT)
gpio.setup(STEP, gpio.OUT)
gpio.output(DIR,CW)

# Main body of code
try:
    #while True:
    #sleep(1)
    gpio.output(DIR,CW)
    for x in range(10):
        gpio.output(STEP,gpio.HIGH)
        sleep(.0100)
        gpio.output(STEP,gpio.LOW)
        sleep(.0100)
    
        sleep(1)
        gpio.output(DIR,CCW)
        for x in range(10):
            gpio.output(STEP,gpio.HIGH)
            sleep(.010)
            gpio.output(STEP,gpio.LOW)
            sleep(.010)
            
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()#Libera de pines GPIO
