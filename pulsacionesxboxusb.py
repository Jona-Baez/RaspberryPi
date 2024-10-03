#Importar biblioteca -evdev- y sus modulos
from evdev import InputDevice, categorize, ecodes

#Crea objeto llamado "gamepad" para almacenar datos
usb = InputDevice('/dev/input/event0')

#Imprime la informacion del dispositivo al inicio
print(usb)

#-evdev- se encuentra en un ciclo monitoreando el gamepad
for event in usb.read_loop():
    print(categorize(event))
