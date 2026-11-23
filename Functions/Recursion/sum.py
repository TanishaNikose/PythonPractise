# 1.Implement a recursive function to calculate the sum of natural numbers from 1 to N.

def fun_sum (n):
    if n == 0:
        return 0
    else:
        return n + fun_sum(n-1)

print(fun_sum(5))