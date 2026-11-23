# 17. Create a program to find the union of two arrays (combine unique elements from both arrays).


list1 = [1,2,3,4,4,5]
list2 = [1,4,2,6,7]

union = [] # 1,2,3,4,5,6,7

for i in list1:
    if i not in union:
        union.append(i)

for j in list2:
    if j not in union:
        union.append(j)


union.sort()
print(union)