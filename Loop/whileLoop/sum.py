# 1.Create a Node.js program to find the sum of natural numbers from 1 to N using a while loop.

endNum = int(input("Enter the last number: "))

i = 1
sum = 0
while i <= endNum:
    sum = sum + i
    i += 1

print(f"sum is {sum}")
