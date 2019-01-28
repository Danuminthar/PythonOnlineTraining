import socket
arkar = socket.gethostname()
print("This computer name is: ",arkar)
kyaw = socket.gethostbyname(arkar)
print("The IP address is: ",kyaw)
print()
try:
    socket_obj=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    for port_address in range(134, 140):
        result=socket_obj.connect_ex("195.19.49.83",53190)
        if result==0:
            print("*****************************************************")
            print("computer open at ip_address: ","195.19.49.83",port_address)
            print("*****************************************************")
            print()
            #socket_obj.close()
        #else:
            #print("ip_address " + kyaw +"is not active")
            #socket_obj.close()
except:
    print("error occur")
socket_obj.close()