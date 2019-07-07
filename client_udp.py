
import socket

host = "192.168.1.42"
port = 8080
data = ("hello")
data = str.encode(data)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while (1):
    s.sendto (data,(host,port))
    
