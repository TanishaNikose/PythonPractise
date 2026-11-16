# 9.Implement a program to rotate an array of integers to the left by a given number of positions.

def left_shift(list1, k):
    n = len(list1)
    if n == 0:
        return list1

    k = k % n
    for j in range(k):
        temp = list1[0]
        for i in range(0, n-1):
            list1[i] = list1[i+1]

        list1[n-1] = temp
    return list1

numbers = [1,2,3,4,5]
print(left_shift(numbers, 1))