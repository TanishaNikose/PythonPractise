# 4. Implement a program to find the common elements between two lists using nested for-loops.

listA = [1,2,3,11]
listB = [5,1,6,2,9,3,11]

for i in range(0, len(listA)):
    for j in range(0, len(listB)):
        if listA[i] == listB[j]:
            print(listA[i])
