# 3.Implement a program to find the GCD (Greatest Common Divisor) of two numbers using a while loop.

a = 3
b = 9

i = 1
gcd = 1

while i <= min(a,b): # min() return the smaller item from an iterable
    if a % i == 0 and b % i == 0:
        gcd = i
    i += 1

print("GDC is ", gcd)