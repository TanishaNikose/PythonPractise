# 12. Implement a method to merge two sorted arrays into a single sorted array.

# # okay for this code because lists are already sorted.
# list1 = [1,2,3,4]
# list2 = [5,6,7,8]

# list3 = list1 + list2
# print(list3)

# here lists are not sorted. 
# need to do:- 

# # using sort method
# list1 = [1,2,3,4]
# list2 = [5,6,7,8]

# sorted_array = list1 + list2

# sorted_array.sort()
# print(sorted_array)

# Without sort()

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

sorted_array = []

# Step 1: Combine both lists
for i in list1:
    sorted_array.append(i)

for j in list2:
    sorted_array.append(j)

# Step 2: Sort using Bubble Sort
n = len(sorted_array)

for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_array[j] > sorted_array[j + 1]:
            sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]

print(sorted_array)