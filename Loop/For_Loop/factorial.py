# 6. Write a Node.js program to find the factorial of a number using a for loop.


input_number = int(input("Enter a number: "))
mul = 1

if input_number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(input_number, 0, -1):
        mul *= i

    print(mul)
