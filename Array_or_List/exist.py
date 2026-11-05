# 4.Implement a Node.js method to check if a given element exists in an array of strings. 

list1 = ["apple", "mango", "banana", "guava"]
searchElement = input("Enter the word you need to search: " ).lower()

if searchElement in list1:
    print("exist")
else:
    print("Not exist")