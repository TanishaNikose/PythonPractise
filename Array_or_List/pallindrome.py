# 14. Create a python method to check if an array is a palindrome (reads the same forwards and backward).

list1 = [1, 2, 3, 2, 1]
list2 = []
for j in list1[::-1]:
    list2 += [j]

if list1 == list2:
   print("This is pallindrome.")
else:
    print("Not pollindrome.")
