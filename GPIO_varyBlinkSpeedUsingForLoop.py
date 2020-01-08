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
            
#ehariono001@e.ntu.edu.sg
#alvin_seoh@bca.gov.sg btn conditioning
#how to always display 2 dec. places even if num is 1 dec place eg. 0.5 show as 0.50?