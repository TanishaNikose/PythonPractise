# 7. Implement a program that prints a pattern of stars in a right-angled triangle using nested for loops.

size = int((input("Enter the size: ")))

for i in range(1, size + 1):
    for j in range(i):
        print("*", end="")
    print()