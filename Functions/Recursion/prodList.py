# 9.Create a recursive function to calculate the product of elements in a list.

def fun_prod(list1):
    if list1 == []:
        return 1
    else:
        return list1[0] * fun_prod(list1[1:])


print(fun_prod([1,2,3,4,5]))