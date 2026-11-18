# Create a program that calculates the average of all even numbers in an array of integers.

list1 = [1,2,3,4,5,6,7]
evenNum = []

for i in list1:
    if i % 2 == 0:
        evenNum.append(i)

print(evenNum)

# finding the sum of even Numbers
even_Num_sum = 0
for i in evenNum:
    even_Num_sum = even_Num_sum + i

print("Sum of Even Numbers is ", even_Num_sum) 

# finding Average
average = (even_Num_sum)/len(evenNum)
print("The average is", average)