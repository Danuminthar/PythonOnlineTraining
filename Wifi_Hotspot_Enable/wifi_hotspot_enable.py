#!/usr/bin/python3

import os
os.system('cls')
print("Wireless Enable")
print()
cmd="0"
while cmd!="3":
    print ("1-start hotspot")
    print("2-stop")
    print ("3-end")
    cmd=input("Please Enter the choice(1,2,3): ")
    if cmd=="1":
        ssid=input("Please Enter SSID: ")
        password=input("Enter Password: ")
        command="netsh wlan set hostednetwork mode=allow ssid=" +ssid + " key="+ password
        os.system(command)
        os.system("netsh wlan start hostednetwork")
    if cmd=="2":
        os.system("netsh wlan stop hostednetwork")
    if cmd=="3":
        quit()

    else:
        print("You can't enter this letter!,Please re-enter")
        print()
        #os.system("pause")