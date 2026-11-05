# 19. Create a program that checks if a given number is positive, even, and a multiple of 7.

num = int(input("Enter Number :- "))
if num > 0:
    if num % 2 == 0 and num % 7 == 0:
        print("Entered number is positive, Even and mul of 7")
    else:
        print("Condition not satisfied.")
else:
    print("Please Enter positive Number")