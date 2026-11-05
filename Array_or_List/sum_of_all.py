# 1.Write a python program to find the sum of all elements in an integer array.

# list = [1,2,3,4]
# sum = 0
# for i in range(0, len(list)):
#     sum = list[i] + sum

# print(f"The sum of array is: {sum}")





# note :- there is difference between List and Array in Python.
# there are multiple ways to create a array in python



# arr = list((1,2,3,4))
# print(arr*2)
# list2 = list("pythonprogramming")
# print(list2)
# zeros = list([0] * 5)
# print(zeros)

from array import array
arr = array('i', [10, 20, 30]) # Here, 'i' means a signed integer type.
print(arr*2)


# import numpy as np 
# arr = np.array([10,20,30,]*2)
# print(arr)