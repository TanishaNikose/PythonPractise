# 2. Write a function that calculates the nth term of the geometric progression (GP) using recursion.

# # without recursion

# multiply = 2
# start_num = 1

# for i in range(5):
#     print(start_num)
#     gp = start_num * multiply
#     start_num = gp


# recursion

def fun_gp(num, count):
   if count == 5:
       return ""
   else:
       print (num)
       return fun_gp(num*2, count + 1)


print(fun_gp(1,0))