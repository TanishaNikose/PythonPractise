# 3.Implement a function that checks if a number is even.

def even(num):
    if num % 2 == 0:
        return "EVEN NUMBER"
    else:
        return "ODD NUMBER"

print(even(12345))