import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s=("hello")
s=str.encode(s)

var=0
host = "192.168.1.41"
port = 5002
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((host,port))
while(1):
    sock.sendto(s,("192.168.1.34",5003))
    var=sock.recvfrom(1024)
    print (var)
