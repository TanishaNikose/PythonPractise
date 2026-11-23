# 10. Write a function to sort an array of strings in alphabetical order.
list1 = ["apple", "mango", "cherry", "pomigranate", "dragon Fruit"]
list1.sort() # it changes the original list and returns None
print(list1) # output :-  ['apple', 'cherry', 'dragon Fruit', 'mango', 'pomigranate']

# need to find the actual logic and difference between sort() and sorted()


# Feature	                             list.sort()	                                      sorted()
# Type	                             List method (my_list.sort())	                      Built-in function (sorted(iterable))
# Supported Types                    Lists only	                                          Any iterable (lists, tuples, strings, sets, dictionaries)
# Original Data	                     Mutates the original list directly	                  Leaves the original data untouched
# Return Value	                     None	                                              A new sorted list
# Memory Efficiency	                 Slightly more efficient (no copy created)	          Uses extra memory to build a new list

# with the help of sorted method

new_list =  sorted(list1)
print(new_list)



# actual logic -- Python compares strings lexicographically, character by character, using their Unicode values. For ordinary lowercase English words, this follows alphabetical order.
print("apple" > "banana")


for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] > list1[j]:
            list1[i] , list1[j] = list1[j], list1[i]

print(list1)


# Sorting Numbers - This code is sorting the numbers correctly but not sorting in the bubble sort exactly

List1 = [7,3,2,6,5]

for i in range(len(List1)):
    for j in range(len(List1)):
        if List1[i] < List1[j]:
            List1[i], List1[j] = List1[j], List1[i]

print(List1)