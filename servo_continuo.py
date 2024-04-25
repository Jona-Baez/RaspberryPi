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
angulo=0
try:
    while True:
        while angulo<180:
            #SUBIDA
            angulo=angulo+10
            print(angulo)
            servo.ChangeDutyCycle(2+(angulo/18))
            sleep(0.5)#Tiempo de espera para preguntar nuevamente
            servo.ChangeDutyCycle(0)
        while angulo>0:
            #BAJADA
            angulo=angulo-10
            print(angulo)
            servo.ChangeDutyCycle(2+(angulo/18))
            sleep(0.5)#Tiempo de espera para preguntar nuevamente
            servo.ChangeDutyCycle(0)
finally:
    servo.stop()
    GPIO.cleanup()
