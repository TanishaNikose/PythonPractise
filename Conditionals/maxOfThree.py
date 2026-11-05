# 4.Implement a program to find the maximum of three numbers using nested if statements.

a = int(input("Enter 1st Num:- "))
b = int(input("Enter 2nd Num:- "))
c = int(input("Enter 3rd Num:- "))

if a >= b:
    if a >= c:
        print(f"{a} is the Greater Number")
    else:
        print(f"{c} is the Greater Number")
else:
     if b >= c:
        print(f"{b} is the Greater Number")
     else:
         print(f"{c} is the Greater Number.")
