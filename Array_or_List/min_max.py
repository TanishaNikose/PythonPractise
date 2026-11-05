# 2.Create an array of integers and find the maximum and minimum values in the array. 

list1 = [3,6,2,8,4]
min = list1[0]
max = list1[0]

for i in list1:
    if i > max:
        max = i
    if i < min:
        min = i

print(f"Minimum is {min}")
print(f"maximum is {max}")