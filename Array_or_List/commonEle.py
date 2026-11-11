# 7.Write a Node.js program to find the common elements between two arrays of integers.

# list1 = [1,2,3,4,5]
# list2 = [5,6,7,1,2,3]
# commonEle = []

# for i in list1:  # this i is taking direct value of the List
#     for j in list2:
#         if i == j:
#             commonEle = commonEle + [i]

# print("Common Elements are ", end="")
# print(commonEle)


list3 = [34,56,46]
list4 = [89,34,78]
commonEle = []

for i in range(len(list3)):  # index based tracking
    for j in range(len(list4)):
        if list3[i] == list4[j]:
            commonEle = commonEle + [list3[i]]

print("Common Elements are ", end ="")
print(commonEle)