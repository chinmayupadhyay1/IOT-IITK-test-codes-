import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s=("hello")
s=str.encode(s)
while(1):
    sock.sendto (s,("192.168.1.34",5003))
