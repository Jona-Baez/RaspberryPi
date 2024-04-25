from evdev import InputDevice, categorize, ecodes

print("PULSA LOS BOTONES DEL GAMEPAD")

#creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event4')

#Variables de codigo de botones
BTN_Y = 308 #1
BTN_X = 307 #2
BTN_B = 305 #3
BTN_A = 304 #4

BTN_TL = 310
BTN_TL2 = 312
BTN_TR = 311
BTN_TR2 = 313

BTN_START = 315
BTN_SELECT = 314



for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == BTN_START:
                print("START")
            elif event.code == BTN_SELECT:
                print("SELECT")
            elif event.code == BTN_TL:
                print("GATILLO IZQUIERDO 1")
            elif event.code == BTN_TL2:
                print("GATILLO IZQUIERDO 2")
            elif event.code == BTN_TR:
                print("GATILLO DERECHO 1")
            elif event.code ==BTN_TR2:
                print("GATILLO DERECHO 2")
            elif event.code == BTN_Y:
                print("1")
            elif event.code == BTN_B:
                print("2")
            elif event.code == BTN_A:
                print("3")
            elif event.code == BTN_X:
                print("4")
