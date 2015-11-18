import RPi.GPIO as GPIO
import time,sys

try:
	PIN_NUMBER = int(sys.argv[1])

	#Set board mode
	GPIO.setmode(GPIO.BCM)

	#set LED pin
	GPIO.setup(PIN_NUMBER,GPIO.OUT)

	#infinite loop
	while True:
        	GPIO.output(PIN_NUMBER,GPIO.HIGH)
        	time.sleep(0.5)
        	GPIO.output(PIN_NUMBER,GPIO.LOW)
        	time.sleep(0.5)
finally:
	print "I was here"
	GPIO.cleanup()
