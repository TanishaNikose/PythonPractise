# 3.Write a program to reverse an array of characters in place.

list1 = ["p","y","t","h","o","n"]

# With the help of method
# list1.reverse()
# print(list1)

# with Actual logic
n = len(list1)
print(n)

for i in range(n // 2):
    list1[i], list1[n-i-1] = list1[n-i-1], list1[i]

print(list1)