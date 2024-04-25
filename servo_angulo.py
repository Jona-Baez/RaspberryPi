#Importamos librerias
import RPi.GPIO as GPIO
from time import sleep
#Establecer el modo de los pines
GPIO.setmode(GPIO.BOARD)
#Declarar los pines y variables
GPIO.setup(8,GPIO.OUT)
servo=GPIO.PWM(8,50)#(pin,Hz)
#Iniciar PWM
servo.start(0)
#Ciclo
try:
    while True:
        #Preguntar al usuario el angulo al que quiere desplazarse
        angulo = int(input('Introduce el angulo al que quieres desplazarse | Entre 0 y 180: '))
        servo.ChangeDutyCycle(angulo)#2+(angulo/18) o 2 a 12
        sleep(1)#Tiempo de espera para preguntar nuevamente
        #servo.ChangeDutyCycle(0)
finally:
    servo.stop()
    GPIO.cleanup()
