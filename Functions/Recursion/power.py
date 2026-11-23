# 5.Create a recursive function to compute the power of a number (a^b).


# hint - 2 pow 3 = 2 * 2 pow 2
#        2 pow 2 = 2 * 2 pow 1

def fun_pow(num, pow):
    # base condition
    if pow == 0:
        return 1
    # recursive call
    else:
        return num * fun_pow(num, pow-1)


print(fun_pow(2,3))