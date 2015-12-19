import RPi.GPIO as GPIO
import time,os
import datetime,subprocess

try:
	#global variables for pins
	#team_1 pin
	TEAM_1=14
	TEAM_1_LIGHT=8

	#team_2 pin
	TEAM_2=15
	TEAM_2_LIGHT=7

	#team_3 pin
	TEAM_3=18
	TEAM_3_LIGHT=12

	#team_4 pin
	TEAM_4=23
	TEAM_4_LIGHT=16

	#reset switch 
	RESET_SWITCH=24
	RESET_LIGHT=25
	reset = False
        p = 0
	def start_Quiz():
		global reset
		reset =  True
		#set the reset LED on
		GPIO.output(RESET_LIGHT,GPIO.HIGH)

	def stop_Quiz():
		global reset
		reset = False
		#stop the reset LED
		GPIO.output(RESET_LIGHT,GPIO.LOW)

	def start_buzzer_light(TEAM_NUMBER_LIGHT):
		GPIO.output(TEAM_NUMBER_LIGHT,GPIO.HIGH)
		
	def stop_buzzer_light(TEAM_NUMBER_LIGHT):
		GPIO.output(TEAM_NUMBER_LIGHT,GPIO.LOW)	
	
	def play_sound():
		os.system('mpg123 -q ../sounds/Wrong-answer-sound-effect.mp3 &')
		time.sleep(1)
	def play_team(team):
		os.system('mpg123 -q ../sounds/team_%d.mp3 &'%team)
		time.sleep(1)
		
	
	GPIO.setmode(GPIO.BCM)

	#config for team switches
	GPIO.setup(TEAM_1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	GPIO.setup(TEAM_2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	GPIO.setup(TEAM_3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	GPIO.setup(TEAM_4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

	#config for light switches
	GPIO.setup(TEAM_1_LIGHT,GPIO.OUT)
	GPIO.setup(TEAM_2_LIGHT,GPIO.OUT)
	GPIO.setup(TEAM_3_LIGHT,GPIO.OUT)
	GPIO.setup(TEAM_4_LIGHT,GPIO.OUT)

	#config for reset switches
	GPIO.setup(RESET_SWITCH,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	GPIO.setup(RESET_LIGHT,GPIO.OUT)

	while True:
		reset_button_state = GPIO.input(RESET_SWITCH)
	
		if reset_button_state == False:
			stop_buzzer_light(TEAM_1_LIGHT)
			stop_buzzer_light(TEAM_2_LIGHT)
			stop_buzzer_light(TEAM_3_LIGHT)
			stop_buzzer_light(TEAM_4_LIGHT)
			start_Quiz()
			time.sleep(0.2)
		else:
			stop_Quiz()

		while reset==True:
		 	team1_input_state =  GPIO.input(TEAM_1)
        	 	team2_input_state =  GPIO.input(TEAM_2)
        	 	team3_input_state =  GPIO.input(TEAM_3)
           	 	team4_input_state =  GPIO.input(TEAM_4)

		 	if team1_input_state == False:
				print('Team 1 '+ datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f'))
				start_buzzer_light(TEAM_1_LIGHT)
				stop_Quiz()
				play_sound()
				play_team(1)
		 	if team2_input_state == False:
		 		print('Team 2 '+ datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f'))
                 		start_buzzer_light(TEAM_2_LIGHT)
				stop_Quiz()
				play_sound()
				play_team(2)
		 	if team3_input_state == False:
                 		print('Team 3 ' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f'))
                 		start_buzzer_light(TEAM_3_LIGHT)
				stop_Quiz()
				play_sound()
				play_team(3)
		 	if team4_input_state == False:
		 		print('Team 4 ' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f'))
		 		start_buzzer_light(TEAM_4_LIGHT)
				stop_Quiz()
				play_sound()
				play_team(4)
		 	#if reset_button_state == False:
				#print('Resetting Again')
				#stop_Quiz()
				#time.sleep(0.2)
				#start_Quiz()

finally:
	GPIO.cleanup()
