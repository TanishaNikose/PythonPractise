# Write a Node.js program to determine if a given number is a prime number.

number = int(input("Enter number :- "))

if number  <= 1:
    print("Number is Not prime.")
else:
    i = 2
    while i <= number/2:
        if number % i == 0:
            print("Number is not prime.")
            break
        i += 1
    else:
        print("Number is prime.")