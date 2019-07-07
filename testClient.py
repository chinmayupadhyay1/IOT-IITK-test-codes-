import socket
host="192.168.1.42"
port=5002
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s=("hello")
s=str.encode(s)
while(1):
    sock.sendto(s,(host,port))
