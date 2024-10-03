from evdev import InputDevice, categorize, ecodes#Bibliotecas jostick
import RPi.GPIO as GPIO
from time import sleep
import subprocess
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)#Pin Led_Inicial
GPIO.output(7,True)#Encender Led_Inicial
GPIO.setup(26,GPIO.OUT)#STAN Buzzer
GPIO.output(26,False)#Apagar Buzzer

gamepad = InputDevice('/dev/input/event0')
BTN_SELECT = 314; BTN_START = 315#Codigos Select y Start
BTN_Y = 308;BTN_B = 305;BTN_A = 304;BTN_X = 307#Codigos Y B A X
BTN_TL = 310;BTN_TR = 311;#Codigos Gatillos Digitales
ABS_Z=2;ABS_RZ=5#Gatillos Analogicos
ABS_HAT0Y=17;ABS_HAT0X=16#Cruceta
ABS_Y=1;ABS_X=0#Ejes joystick Izquierda
ABS_RY=4;ABS_RX=3#Ejes joystick Derecha

#STEPPER
#Pines de fin de carrera
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_UP)
pinDir=16;pinStep=18#Pines
GPIO.setup(pinDir, GPIO.OUT)#Salidas del stepper
GPIO.setup(pinStep, GPIO.OUT)#Salidas del stepper
#SERVO
GPIO.setup(13,GPIO.OUT)#Pin Servo
servo=GPIO.PWM(13,50)#(pin,Hz)
servo.start(0)#Inicia PWM
maximo=120#Angulo maximo
minimo=50#Angulo minimo
angulo=80#Angulo inicial
servo.ChangeDutyCycle(2+(angulo/18))#Metodo para mover el servo al angulo indicado
sleep(0.5)
servo.ChangeDutyCycle(0)#Ciclo util del servo (Para que no vibre)

print("PULSA LOS BOTONES DEL JOYSTICK")    
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == BTN_SELECT:#Botones Digitales
                print("SELECT",event.code)
            elif event.code == BTN_START:
                print("START",event.code)
            elif event.code == BTN_Y:
                print("Y",event.code)
            elif event.code == BTN_B:
                print("B",event.code)
            elif event.code == BTN_A:
                print("A",event.code)
            elif event.code == BTN_X:
                print("X",event.code)
            #elif event.code == BTN_TL:
             #   print("GATILLO IZQUIERDO DIGITAL",event.code)
            #elif event.code == BTN_TR:
             #   print("GATILLO DERECHO DIGITAL",event.code)
            elif event.code ==(BTN_TL and BTN_TR):
                    print("Los 2 gatillos digitales",event.code)
                    print("Se va a apagar")
                    subprocess.call(['sudo','shutdown','now'])
        
    elif event.type == ecodes.EV_ABS:
        if event.value == 1:#Cruceta Abajo y Derecha 
            if event.code == ABS_HAT0Y:
                print("Abajo cruceta",event.code)
            elif event.code == ABS_HAT0X:
                print("Derecha cruceta",event.code)
        if event.value == -1:#Cruceta Arriba e Izquierda
            if event.code == ABS_HAT0Y:
                print("Arriba cruceta",event.code)
            elif event.code == ABS_HAT0X:
                print("Izquierda cruceta",event.code)
        if (-32768<=event.value <0):#Arribas e Izquierdas
            if event.code == ABS_Y:
                print("Arriba Eje",event.code)
                GPIO.output(pinDir,0)
                for i in range(0,20):#Cantidad de pulsos
                    GPIO.output(pinStep, True)
                    sleep(0.005)
                    GPIO.output(pinStep, False)
                    sleep(0.005)
            elif event.code == ABS_X:
                print("Izquierda Eje",event.code)#####
                if (angulo<maximo):
                        angulo=angulo+10
                        servo.ChangeDutyCycle(2+(angulo/18))
                        print(angulo,"grados")
                        sleep(0.5)
                        servo.ChangeDutyCycle(0)
            elif event.code == ABS_RX:
                print("Eje X",event.code)
            elif event.code == ABS_RY:
                print("Eje Y",event.code)
        if (0<event.value <=32768):#Abajos y Derechas
            if event.code == ABS_Y:
                #print("Abajo eje",event.code)
                 if GPIO.input(19)==True and GPIO.input(21)==True and GPIO.input(15)==True and GPIO.input(12)==True:
                        print("Abajo "+"Sin bloqueo",event.code)
                        GPIO.output(pinDir, 1)
                        for i in range(0,20):#Cantidad de pulsos
                            GPIO.output(pinStep, True)
                            sleep(0.005)
                            GPIO.output(pinStep, False)
                            sleep(0.005)
                 #Pines para bloquear (botones)
                 elif GPIO.input(12)==False:
                    print("Bloqueado")
                 elif GPIO.input(15)==False:
                    print("Bloqueado")
                 elif GPIO.input(19)==False:
                    print("Bloqueado")
                 elif GPIO.input(21)==False:
                    print("Bloqueado") 
            elif event.code == ABS_X:
                print("Derecha eje",event.code)#####
                if (angulo>minimo):
                        angulo=angulo-10
                        servo.ChangeDutyCycle(2+(angulo/18))
                        print(angulo, "grados")
                        sleep(0.5)
                        servo.ChangeDutyCycle(0)
            elif event.code == ABS_RX:
                print("Eje B",event.code)
            elif event.code == ABS_RY:
                print("Eje A",event.code)
        if (0<event.value <=1024):#Gatillos Analogicos
            if event.code == ABS_Z:
                print("GATTILLO ANALOGICO IZQUIERDA",event.code)
            elif event.code == ABS_RZ:
                print("GATILLO ANALOGICO DERECHA",event.code)
            
