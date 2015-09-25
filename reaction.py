import RPi.GPIO as GPIO
import time
import random


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4
right_button = 14
left_button = 15

GPIO.setup(led, GPIO.OUT)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)


GPIO.output(led, 1)
time.sleep(random.uniform(5, 10))


while True:
    if GPIO.input(left_button) == False:
        print("Left button pressed")
        GPIO.output(led, 0)
        break
    if GPIO.input(right_button) == False:
        print("Right button pressed")
        GPIO.output(led, 0)
        break
    



GPIO.cleanup()
