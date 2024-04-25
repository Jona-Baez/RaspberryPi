#Dimmer de un LED
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)

p = GPIO.PWM(40, 100)  
p.start(True)
try:
    while True:
        for i in range(0, 101, 5):
            p.ChangeDutyCycle(i)
            sleep(0.1)
        for i in range(100, -1, -5):
            p.ChangeDutyCycle(i)
            sleep(0.1)
except KeyboardInterrupt:
    print("El programa termino")
p.stop()
GPIO.cleanup()
