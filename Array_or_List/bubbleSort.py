list1 = [5,6,3,2,8]

for i in range(len(list1)):
    for j in range(len(list1)-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] =  list1[j+1], list1[j]

print(list1)