# 19. Write a program to rearrange an array so that all even elements come before odd elements.

# # By created a new array
# list1 = [1,2,3,4,5,6]

# evenArr = []
# oddArr = []

# for i in list1:
#     if i % 2 == 0:
#         evenArr.append(i)
#     else:
#         oddArr.append(i)

# print(evenArr)
# print(oddArr)

# arrangedList = evenArr + oddArr
# print(arrangedList)

# by trying an existed array

list1 = [1,2,3,4,5,6]

evenArr = []
oddArr = []

for i in list1:
    if i % 2 == 0:
        evenArr.append(i)
    else:
        oddArr.append(i)

list1 = evenArr + oddArr
print(list1)

# This can also be solve using two prointer approach.