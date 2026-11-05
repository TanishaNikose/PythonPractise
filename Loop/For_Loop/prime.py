# 10. Implement a program to check if a given number is prime using a for loop.

num = int(input("Enter a number: "))
temp = 0

if num <= 1:
    print("1 is not a prime number")
else:
    for i in range(2, (num//2)+1):
        if num % i == 0:
            temp = 1
            break

    if temp == 1:
        print("Not prime")
    else:
        print("prime")