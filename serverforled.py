import socket
import RPi.GPIO as GPIO
import time

var=0
host = "192.168.1.41"
port = 8080
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((host,port))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
p = GPIO.PWM(33,50)
p.start(0)

while(1):
   var=sock.recvfrom(1024)
   var = (float(var[0]))
   print(var)
   p.ChangeDutyCycle(var)


##try:
## while (1):
##        for i in range(100):
##                    p.ChangeDutyCycle(i)
##                    time.sleep(0.02)
##        for i in range(100):
##                     p.ChangeDutyCycle(100-i)
##                     time.sleep(0.02)
##except KeyboardInterrupt:
##        pass
p.stop()
GPIO.cleanup()
             

             
