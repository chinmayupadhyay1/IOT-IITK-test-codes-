#blink.py
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
while(1):
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, True)
    time.sleep(1)
    GPIO.output(4, False)
    time.sleep(1)
