#step 1: import libs for GPIO
import RPi.GPIO as GPIO
from time import sleep #used to pause your code at a particular line

GPIO.setmode(GPIO.BOARD) #tells py program to ref pins using BOARD convention
GPIO.setup(11,GPIO.OUT) #defines pin 11 as an output pin to send sig out
GPIO.setup(13,GPIO.OUT)
#ledPWM = GPIO.PWM(11, 500)
#ledPWM.start(100)

brightness=100
stepSize=-5
#PWM while True block
while True:
	GPIO.output(11,1)
	GPIO.output(13,0)
	sleep(1)
	GPIO.output(11,0)
	GPIO.output(13,1)
	sleep(1)
'''
while True:
	ledPWM.changeDutyCycle(brightness)
	brightness = brightness + stepSize
	if brightness == 0 or brightness == 100:
		stepSize = -stepSize
	sleep(0.01)
'''
'''
while True:
	GPIO.output(11, 1) #sends a HIGH sig out to pin 1
	sleep(speed)
	GPIO.output(11,0) 
	sleep(speed)
'''
