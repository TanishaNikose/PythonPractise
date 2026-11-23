# 4.Implement a recursive function to calculate the factorial of a number.

# 5 * 4 *3 * 2* 1 --  factorial of 5
def fun_fact(n):
    if n == 1:
        return 1
    else:
        return n * fun_fact(n-1)

print(fun_fact(5))