from evdev import InputDevice, categorize, ecodes

print("PULSA LOS BOTONES DEL JOYSTICK")

#creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event4')

#Variables de codigo de botones 1,2,3 y4
BTN_JOYSTICK = 288;
BTN_THUMB = 289;
BTN_THUMB2 = 290;
BTN_TOP = 291
#Variables de codigo de botones Gatillos
BTN_TOP2 = 292;BTN_PINKIE = 293;BTN_BASE = 294;BTN_BASE2 = 295
#Variables de codigo de botones Select y Start
BTN_BASE3 = 296;BTN_BASE4 = 297
#Variables de codigo de botones Ejes
ABS_Y=1
ABS_X=0

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == BTN_BASE3:
                print("SELECT")
            elif event.code == BTN_BASE4:
                print("START")
            elif event.code == BTN_TOP2:
                print("GATILLO IZQUIERDO 1")
            elif event.code == BTN_BASE:
                print("GATILLO IZQUIERDO 2")
            elif event.code == BTN_PINKIE:
                print("GATILLO DERECHO 1")
            elif event.code ==BTN_BASE2:
                print("GATILLO DERECHO 2")
            elif event.code == BTN_JOYSTICK:
                for i in range (event.code == BTN_JOYSTICK):
                    print("1")
            elif event.code == BTN_THUMB:
                print("2")
            elif event.code == BTN_THUMB2:
                print("3")
            elif event.code == BTN_TOP:
                print("4")
    elif event.type == ecodes.EV_ABS:
        if event.value == 0:
            if event.code == ABS_Y:
                print("Arriba")
            elif event.code == ABS_X:
                print("Izquierda")
        if event.value == 255:
            if event.code == ABS_Y:
                print("Abajo")
            elif event.code == ABS_X:
                print("Derecha")
