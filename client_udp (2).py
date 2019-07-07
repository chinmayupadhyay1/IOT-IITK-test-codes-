import socket
import time 

host = "198.168.1.41"
port = 8080
data = input("what percentage do you want? ").encode()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while (1):
    s.sendto (data,(host,port))
    time.sleep(1)
