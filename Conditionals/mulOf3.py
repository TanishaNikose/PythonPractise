# 12. Implement a program to check whether a number is even and a multiple of 3.

number = int(input("Enter the number: "))
if number % 2 == 0 and number % 3 == 0:
    print("Entered number is Even and mul of 3")
else:
    print("The number is not satified both the conditions.")
