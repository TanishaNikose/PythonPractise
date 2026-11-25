# 5. Write a Node.js function to calculate the number of ways to climb a staircase with N steps, considering you can take 1 or 2 steps at a time.


# 0,1,1,2,3,5,8,13

def staircase(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return staircase(n-1) + staircase(n-2)

print("The ways are ", staircase(4))