import subprocess,time

TEAM_NUMBER_LIGHT = 7
p = subprocess.Popen(["sudo","python","blink_led.py",str(TEAM_NUMBER_LIGHT)])
time.sleep(5)
p.kill()
