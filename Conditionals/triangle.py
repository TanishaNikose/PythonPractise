# 15. Implement a program that determines if a triangle is equilateral, isosceles, or scalene based on the side lengths.

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the Third side: "))

if a == b and b == c:
    print("Equilateral Triangle.")
elif a != b and b != c and a != c:
    print("Scelene Trianle")
else:
    print("Isoscelen Triangle")