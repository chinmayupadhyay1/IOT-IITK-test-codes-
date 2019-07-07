import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(33, GPIO.OUT)

p = GPIO.PWM(33,50)

p.start(0)
p.ChangeDutyCycle(100)



             
