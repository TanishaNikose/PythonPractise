# 18. Implement a method to find the intersection of two arrays (common elements in both arrays).

list1 = [1,2,3,4,5]
list2 = [2,4,1,6,7]

intersection = []

for i in list1:
    for j in list2:
        if i == j:
            intersection.append(i)

print(intersection)