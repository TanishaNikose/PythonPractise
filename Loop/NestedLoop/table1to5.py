# 1. Implement a program to print a multiplication table for numbers 1 to 5 using nested for-loops.

startNum  = int(input("Enter the startNum: "))
endNum  = int(input("Enter the endNum: "))

for i in range(startNum, endNum+1):
    print("Table of ",i)
    for j in range(1, 11):
        tab = i * j
        print(i , "*", j, "=", tab)