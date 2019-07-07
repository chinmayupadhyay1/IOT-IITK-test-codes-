import socket
var=0
host1 = "192.168.1.41"
host2 = "192.168.1.42"
port = 5002
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((host1,port))
while(1):
    var=sock.recvfrom(1024)
    print (var[0])   
    s=(var)
    s=s.encode(s)
    sock.sendto (s,(host2,5002))
