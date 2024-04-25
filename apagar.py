import RPi.GPIO as GPIO
import subprocess
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(36,GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:	
	if GPIO.input(36)==False:
		print("La Raspberry Pi se apagará")
		subprocess.call(['sudo','shutdown','now'])
