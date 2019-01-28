#!/usr/bin/python3
import socket
arkar=socket.gethostname()
print(arkar)
print("Arkar's IP address: ")
print(socket.gethostbyname(arkar))
print("Google's IP address: ")
print(socket.gethostbyname("www.google.com"))
print("My blog website IP address: ")
print(socket.gethostbyname("sarroakmyar.blogspot.com"))
try:
    ip_address=socket.gethostbyname(arkar)
    print("My computer IP address is: ",ip_address)
except:
    print("Error is occured")