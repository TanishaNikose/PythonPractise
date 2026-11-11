# # 8.Create a method to shift all the elements of an integer array to the right by a specified number of positions.

# # for changing one single shift to right

# list1 = [1,2,3,4,5]
# temp = list1[-1]

# for i in range(len(list1)-1, 0, -1):
#     list1[i] = list1[i-1]

# list1[0] = temp
# print(list1)


# making it more modular


def shift_right(list1, k):

    n = len(list1)

    if n == 0:
        return list1

    k = k % n

    for j in range(k):

        temp = list1[-1]

        for i in range(n-1, 0, -1):
            list1[i] = list1[i-1]

        list1[0] = temp

    return list1



numbers = [1, 2, 3, 4, 5]

print(shift_right(numbers, 4))