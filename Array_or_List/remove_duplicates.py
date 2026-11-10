# 5.Write a program to remove duplicates from an array of integers.

list1 = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6]
newList  = []

for i in list1:
  if i not in newList:
    # newList.append(i)
    newList = newList + [i]

print(newList)


# making change in the existing Array or List

# list1 = [1, 2, 2, 3, 3, 3, 4, 4, 5]

# i = 0

# while i < len(list1):
#     if list1[i] in list1[i+1:]:
#         list1.pop(i)
#     else:
#         i += 1

# print(list1)