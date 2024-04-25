import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#Ahorita se encuentra el configuracion Pull Down
#Si queremos cambiar de configuracion a Pull Up
#sera necesario cambiar a: GPIO.PUD_UP
while True:
	GPIO.output(8,GPIO.input(10))
