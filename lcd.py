import time
import lcdlibreria as LCD

def main():
  LCD.lcd_init()
  tiempo=int(input("Ingresa el tiempo"))
  for i in range (1,tiempo+1):
    LCD.lcd_texto("Tiempo restante:",LCD.LINE_1)
    LCD.lcd_texto(" 0 "+"min  "+str(i)+" seg",LCD.LINE_2)
    int(str(i))
    i+=1    
    time.sleep(1)
  LCD.lcd_texto("Hasta luego",LCD.LINE_1)
  LCD.lcd_texto("Vuelva pronto :D" ,LCD.LINE_2)
  time.sleep(1)

try:
   main()
except KeyboardInterrupt:
  pass
finally:
  LCD.lcd_write(0x01, LCD.LCD_CMD)
  LCD.lcd_texto("   FIN DE LA   ",LCD.LINE_1)
  LCD.lcd_texto("  JORNADA  :D  " ,LCD.LINE_2)
  LCD.GPIO.cleanup()
