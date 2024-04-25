#Importar biblioteca -evdev- y sus modulos
from evdev import InputDevice, categorize, ecodes

#Crea objeto llamado "gamepad" para almacenar datos
gamepad = InputDevice('/dev/input/event3')

#Imprime la informacion del dispositivo al inicio
print(gamepad)

#-evdev- se encuentra en un ciclo monitoreando el gamepad
for event in gamepad.read_loop():
    print(categorize(event))
