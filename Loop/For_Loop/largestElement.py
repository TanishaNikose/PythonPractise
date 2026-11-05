# 9. Write a Node.js program to find the largest element in a list using a for loop.

list = [1,2,8,5,3]
largest = list[0]
for i in list:
    if largest < i :
        largest = i

print(largest)
