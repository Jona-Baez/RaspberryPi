from evdev import InputDevice, categorize, ecodes#Bibliotecas jostick
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
gamepad = InputDevice('/dev/input/event0')#Objeto 'gamepad' para obtener eventos
BTN_SELECT = 314; BTN_START = 315#Codigos Select y Start
BTN_Y = 308;BTN_B = 305;BTN_A = 304;BTN_X = 307#Codigos Y B A X
BTN_TL = 310;BTN_TR = 311;#Codigos Gatillos Digitales
ABS_Z=2;ABS_RZ=5#Gatillos Analogicos
ABS_HAT0Y=17;ABS_HAT0X=16#Cruceta
ABS_Y=1;ABS_X=0#Ejes joystick Izquierda
ABS_RY=4;ABS_RX=3#Ejes joystick Derecha

print("PULSA LOS BOTONES DEL JOYSTICK") 
   
while event in gamepad.read_loop():
	if event.code == BTN_B:
		while event.value==1:
			print("B")
	if event.code == BTN_Y:
		while event.value==1:
			print("Y")
				#event.type == ecodes.EV_KEY and event.value == 1 and 
