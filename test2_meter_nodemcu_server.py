import socket
var=0
host = "192.168.1.47"
port = 5002
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((host,port))
while(1):
    var=sock.recvfrom(1024)
    print (var)
