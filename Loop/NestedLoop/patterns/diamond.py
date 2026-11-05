# 2. Create a program to print a pattern of stars in a diamond shape using nested for loops.

# To print diamond, just need to understand two things here
# (1) spaces " "
# (2) Increasing or Decreasing starts

# Notice that diamond has two parts: 
# Upper half ---> Spaces Decreses and stars Increases
# Lower Half ---> spaces Increases and stars Decreases


endnum = int(input("Enter endNum: "))

# Upper half
for i in range(1, endnum+1):

    # print spaces before the stars
    for j in range(endnum - i):
        print(" ", end="")
    # print stars
    for k in range(2 * i - 1):
        print("*", end="")

    print()

# Lower Half 
for i in range(endnum - 1, 0, -1):
    # for spaces
    for j in range(endnum - i):
        print(" ", end="")

    # for stars
    for k in range(2 * i - 1):
        print("*", end="")

    print()