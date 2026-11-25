# # 1. Create a recursive function to find the binary representation of a decimal number.

# How to calculate the binary representation of the  decimal number.
# Understand the rule for calculate it : -

# To convert a decimal number into binary:
# 1. Divide the number by 2.
# 2. Write down the remainder (it will always be 0 or 1).
# 3. Take the quotient and divide it by 2 again.
# 4. Continue until the quotient becomes 0.
# 5. Read all the remainders from bottom to top.


# # without Funciton/recursion
# number = 10
# binary = ""

# while number > 0:
#     remainder = number % 2
#     binary = str(remainder) + binary
#     number = number //2
# else: # will run once loop will complite.
#     print("Loop completed")

# print(binary)

# with rercursive function

def fun_binary(num):
    if num == 0:
        return 
    else:
        fun_binary (num // 2)
        print(num % 2, end="")

fun_binary(4)

    
