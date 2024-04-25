#Dimmer de un LED
from gpiozero import MCP3008
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)

pot = MCP3008(0)
p = GPIO.PWM(40, 100)  
p.start(True)
try:
    while True:
        p.ChangeDutyCycle(pot.values)
        #sleep(0.1)
except KeyboardInterrupt:
    print("El programa termino")
p.stop()
GPIO.cleanup()
