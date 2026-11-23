# 15. Implement a program to find the index of a specific element in an array of integers.

# With the help of the index()

list2 = [1,2,3,4,5]
element = 2
index = list2.index(element)
print(index , "is the index of ", element)


# Logic
list1 = [1,2,3,4,5,6,7]
specific_element  = 7

if specific_element in list1:
    for i in range(len(list1)):
        if list1[i] == specific_element:
            print(f"{i} is the index of {specific_element}")
else:
    print("The element is not in the list")

