#!/usr/bin/python3
# Even Odd program


num1 = 0
while num1 >= 0:
    num1 = int(input("Enter the number: "))
    if num1 % 2 == 0:
        print("Even number")
    else:
        print("odd number")