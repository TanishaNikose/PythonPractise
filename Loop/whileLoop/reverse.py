# 2.Write a program to reverse a given number using a while loop.

num = int(input("Enter the Number: "))
tempNum = num
rev = 0

while tempNum > 0:
    rem = tempNum % 10
    tempNum = tempNum // 10
    rev = rev * 10 + rem

print(rev)