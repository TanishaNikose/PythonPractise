# 3. Implement a recursive function to generate the nth term of an arithmetic progression (AP).


def fun_Ap(num, count):
   if count == 5:
       return 
   else:
       print (num)
       return fun_Ap(num+5, count + 1)


print(fun_Ap(1,0))