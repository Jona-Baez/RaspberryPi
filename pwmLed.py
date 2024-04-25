#Encender y apagar un LED cada cierto tiempo
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)

p=GPIO.PWM(40,0.5)#f=1/s
p.start(True)
input("Oprima la tecla enter para salir")
p.stop()
GPIO.cleanup()
