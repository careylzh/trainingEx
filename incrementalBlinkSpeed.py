import RPi.GPIO as GPIO #name the imported lib as a shortform 'RPi'
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
while True:
    x = 0.05
    while x < 1:
        x = x + 0.05
        GPIO.output(11, True)
        time.sleep(x)
        GPIO.output(11, False)
        time.sleep(x)
        print('speed: ', round(x,2) ) #round x to 2 decimal places 
