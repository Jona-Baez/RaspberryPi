import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Dir=35
Step=37
No_Steps=200
pausa=0.005

# Establecemos direcciones de los pines a usar
GPIO.setup(Dir, GPIO.OUT)
GPIO.setup(Step, GPIO.OUT)

# Hacemos giro en sentido antihorario
while True:
    GPIO.output(Dir,0)
    for i in range(0,No_Steps):
        GPIO.output(Step, True)
        sleep(0.005)
        GPIO.output(Step, False)
        sleep(0.005)

    # Hacemos giro en sentido horario
    GPIO.output(Dir, 1)
    for i in range(0,No_Steps):
        GPIO.output(Step, True)
        sleep(0.005)
        GPIO.output(Step, False)
        sleep(0.005)

GPIO.cleanup() 
