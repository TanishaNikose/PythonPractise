# 13. Write a program to find the frequency of each element in an array of integers.

list1 = [1,7,2,1,3,5,2,6,1,6]

for i in range(len(list1)):

    if list1[i] in list1[:i]:
        continue

    freq = 0
    for j in range(len(list1)):
        if list1[i] == list1[j]:
            freq += 1
    print(f"frequency of {list1[i]} is", freq)
    
