import RPi.GPIO as GPIO
import time,sys

PIN_NUMBER = int(sys.argv[1])

#Set board mode
GPIO.setmode(GPIO.BCM)

#set LED pin
GPIO.setup(PIN_NUMBER,GPIO.OUT)

#infinite loop
GPIO.output(PIN_NUMBER,GPIO.LOW)

GPIO.cleanup()
