import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)

def Prender(NumVeces,Velocidad):
  for i in range(0,NumVeces):
    GPIO.output(15,True)
    time.sleep(Velocidad)
    GPIO.output(15,False)
    time.sleep(Velocidad)
  GPIO.cleanup()

Prender(20,0.5)  
