#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
pin = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
try:
    print('Pin {}is going HIGH'.format(pin))
    GPIO.output(pin, GPIO.HIGH)
    raw_input('press enter when ready:')

    print('Pin {}is going LOW'.format(pin))
    GPIO.output(pin, GPIO.LOW)
    raw_input('press enter when ready:')
finally:
    print('Now doing cleanup before exiting')
    GPIO.cleanup

    
