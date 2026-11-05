# 5. Create a program that generates Pascal's Triangle for a given number of rows using nested for loops.


endnum = 5

previous = []

for i in range(1, endnum + 1):
    current = []

    # Print spaces
    for j in range(endnum - i):
        print(" ", end="")

    # Calculate numbers
    for k in range(i):
        if k == 0 or k == i - 1:
            num = 1
        else:
            num = previous[k - 1] + previous[k]

        current.append(num)
        print(num, end=" ")

    print()
    previous = current
