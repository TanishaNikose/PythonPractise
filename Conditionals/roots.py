# 25. Create a program that calculates the roots of a quadratic equation based on the values of a, b, and c, handling cases where the equation has real or complex roots.

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b**2 - 4*a*c 

if d > 0:
    print("Two distint real roots.")
elif d == 0:
    print("Two equal real roots.")
else:
    print("Two complex roots.")

