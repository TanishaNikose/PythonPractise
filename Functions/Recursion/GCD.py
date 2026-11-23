# 11. Implement a recursive function to calculate the greatest common divisor (GCD) of two numbers.

# GCD stands for Greatest Common Divisor. It is the largest number that can divide two numbers completely (without leaving a remainder).

# # without recursion
# num1 = 20
# num2 = 18

# gcd = 1

# for i in range(1, min(num1, num2)+1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i

# print("GCD", i)


# using recursin
# GCD(a,b) = GCD(b, a % b)

def fun_gcd(a,b):
    if b == 0:
        return a
    else:
        return fun_gcd(b, a % b)

print(fun_gcd(12,18))