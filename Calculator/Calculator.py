#!#/usr/bin/python3
#Calculator
while 2:
    first_num=float(input("Enter The First Number: "))
    operator =input ("Enter the operator: ")
    second_num=float(input("Enter the Second Number: "))
    if operator=="+":
        result=first_num+second_num
    elif operator=="-":
        result=first_num-second_num
    elif operator == "*":
        result = first_num *second_num
    elif operator == "/":
        result = first_num / second_num
    else:
        print("wrong operator")

    print("Result is: ", result)