import RPi.GPIO as GPIO
import time

def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4,GPIO.OUT)

def loop():
        GPIO.output(4,True)
        time.sleep(1)
        GPIO.output(4,False)
        time.sleep(0.5)
        GPIO.output(4,True)
        time.sleep(0.25)
        GPIO.output(4,False)
        time.sleep(0.5)
        GPIO.output(4,True)
        time.sleep(1)
        GPIO.output(4,False)
        time.sleep(0.5)
        
setup()
while True:
        loop()