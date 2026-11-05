# 6.Implement a function to find the second largest element in an array of integers.

list1 = [1, 2, 5, 6, 7]

largest = list1[0]
secondLargest = None

for i in list1[1:]:
    if i > largest:
        secondLargest = largest
        largest = i

    elif secondLargest is None or i > secondLargest:
        if i != largest:
            secondLargest = i

print("Second Largest:", secondLargest)