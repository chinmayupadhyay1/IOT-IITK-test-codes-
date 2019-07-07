import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(33, GPIO.OUT)



p.start(0)
p = GPIO.PWM(33,50)
##
##try:
##    while True:
##               for i in range(100):
##                       p.ChangeDutyCycle(i)
##                       time.sleep(0.02)
##               for i in range(100):
##                       p.ChangeDutyCycle(100-i)
##                       time.sleep(0.02)
##except KeyboardInterrupt:
##       pass
p.stop()
GPIO.cleanup()

             

