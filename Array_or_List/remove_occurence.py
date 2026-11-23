# 16. Write a function to remove all occurrences of a specific element from an array of integers.

# By creating new List
# list1 = [1,2,3,1,5,6,7,1]
# specific_element = 1

# newList = []

# for i in list1:
#     if i == specific_element:
#         continue
#     else:
#         newList = newList + [i]

# print(newList)

# modified existing list
list1 = [1,2,3,1,5,6,7,1]
specific_element = 1

i = 0
while i < len(list1):
    if list1[i] == specific_element:
        list1.pop(i)
    else:
        i = i + 1 

print(list1)