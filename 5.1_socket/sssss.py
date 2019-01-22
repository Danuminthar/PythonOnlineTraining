#!/usr/bin/python3
import socket
#print(socket.gethostname())
#print(socket.gethostbyname("https://saoakmyar.blogspot.com/"))
hostname=socket.gethostname()
try:
    ip_address=socket.gethostbyname_ex(hostname)
    print("IPv4 address is: "+str(ip_address[2][0]))
except:
    print("error")

try:
    ip_address = socket.gethostbyname(hostname)
    print("IPv4 address is: " + format(str(ip_address)))
except:
    print("error")