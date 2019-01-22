#!/usr/bin/python3
print("Wifi_Enable_Program")
print()
import os
os.system("cls")
cmd="0"
while cmd!="3":
    print("1-to start enable wifi")
    print("2-to stop enable wifi")
    print("3-to quit")
    cmd=input("Enter number (1,2,3) to choice option: ")
    if cmd=="1":
        SSID= input ("Please Enter SSID: ")
        Password=input ("Please Enter Password: ")
        command="netsh wlan set hostednetwork mode=allow ssid=" + SSID + "key=" +Password
        os.system(command)
        os.system("netsh wlan start hostednetwork")
    elif cmd=="2":
        os.system("netsh wlan stop hostednetwork")
    elif cmd=="3":
        quit()
    else:
        print("You entered wrong number, Please try again")
        os.system("pause")
        print()

