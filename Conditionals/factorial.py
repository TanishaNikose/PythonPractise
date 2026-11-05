# Create a program to calculate the factorial of a number using an if-else loop.

number = int(input("Enter the Number :- "))

if number > 0:
    prod = 1
    for i in range(1,number+1):
        prod = prod * i

    print(f"The factorial of {number} is {prod}")
else:
    print("please Enter the number larger than 0")
