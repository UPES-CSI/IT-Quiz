import RPi.GPIO as GPIO
import sys,time

PIN_NUMBER = int(sys.argv[1])
GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN_NUMBER,GPIO.IN,pull_up_down=GPIO.PUD_UP)
try:
	while True:
    		input_state = GPIO.input(PIN_NUMBER)
    		if input_state == False:
        		print('Button Pressed')
        		time.sleep(0.2)

except:
	GPIO.cleanup()
