#Lectura del valor del potenciometro
from gpiozero import MCP3008,PWMLED
pot=MCP3008(channel=0)
led=PWMLED(21)
while True:
	print(round(pot.value,2))
#Ajuste de brillo de LED	
from gpiozero import MCP3008,PWMLED
pot=MCP3008(channel=0)
led=PWMLED(21)
while True:
	led.value=pot.value
