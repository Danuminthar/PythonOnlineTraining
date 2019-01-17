#!/usr/bin/python3

import os
os.system('cls')
print("Wireless Enable")
print()

os.system("netsh wlan set hostednetwork mode=allow ssid=Arkar key=12345678")
os.system("netsh wlan start hostednetwork")