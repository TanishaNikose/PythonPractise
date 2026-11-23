# 2.Create a recursive function to find the nth Fibonacci number.

def fun_fibo(n):
    # base condition
    if n == 1:
        return 1
    if n == 0:
        return 0
    # recursive case
    else:
        return fun_fibo(n-1) + fun_fibo(n-2)

print(f"The nth term is ", fun_fibo(6))    



for i in range(6):
    print(fun_fibo(i), end=",")