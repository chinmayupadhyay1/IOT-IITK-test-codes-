import RPi.GPIO as GPIO
import time
import socket

host = 192.168.1.41
port = 8080
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))


GPIO.setmode(GPIO.BOARD)

GPIO.setup(33, GPIO.OUT)

while(1):
    var=s.recvfrom(1024)
    p = GPIO.PWM(33,var)
    p.start(0)
    while(1):
            for i in range(100):
                       p.ChangeDutyCycle(i)
                       time.sleep(0.02)
            for i in range(100):
                       p.ChangeDutyCycle(100-i)
                       time.sleep(0.02)
except KeyboardInterrupt:
       pass
p.stop()
GPIO.cleanup()

             
        
    


             
 
