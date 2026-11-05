# 8. Create a program that generates a list of squares for the numbers from 1 to 10 using a for loop.

# With the help of nested loop
for i in range(1, 10 + 1):
    for j in range(i):
        result = i ** 2

    print(result)


# with the help of single loop

squares = []
for i in range(1,11):
    result = i ** 2
    squares.append(result)


print(squares)