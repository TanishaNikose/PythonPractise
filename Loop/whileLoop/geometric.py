# 5.Write a Python program to find the first N terms of the geometric progression (GP) using a while loop.

# A Geometric Progression (GP) is a sequence in which each term is obtained by multiplying the previous term by a fixed number, called the common ratio.


startNum = 1

# for i in range (1,11):
#     print(startNum)
#     startNum = startNum * 3

i = 1
startNum = int(input("Enter the StartNum: "))
ratio = int(input("Enter the common ratio: "))

while i <= 10:
    print(startNum)
    startNum = startNum * ratio
    i += 1
