import socket

host = "192.168.1.41"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while (1):
    data = (input("give percentage "))
    data = str.encode(data)
    s.sendto (data,(host,port))
    
