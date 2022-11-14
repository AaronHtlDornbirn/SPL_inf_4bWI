import RPi.GPIO as GPIO
import time

def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4,GPIO.OUT)
        GPIO.output(4,False)

        print("Geben sie e für Licht ein und a für Licht aus ein!")

def changeState(state):
    GPIO.output(4,state)
        
setup()
while True:
    _state = str(input())
    if _state == "e":
        changeState(True)
    elif _state == "a":
        changeState(False)
    else:
        print("Falsche Eingabe!")