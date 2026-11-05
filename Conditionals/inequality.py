# 21. Write a Node.js program that takes three numbers as input and determines if they can form a valid triangle based on the triangle inequality theorem.
# Theoram :-  The sum of any two sides must be strictly greater than the third side, not greater than or equal to it.


a = int(input("Enter first side:- "))
b = int(input("Enter Second side:- "))
c = int(input("Enter Third side:- "))

if a <= 0 or b <= 0 or c <= 0:
    print("Side cant be zero")
else:
    if a + b > c and b + c > a and a + c > b:
        print("It satisfied the trianlge theoram.")
    else:
        print("It does not satisfied the trianlge theoram.")



