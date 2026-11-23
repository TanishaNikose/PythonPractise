# 3.Write a recursive function to reverse a string.

# recursive Funciton for reversing the string

def fun_rev(str):
    if str == "":
        return ""
    else:
        return fun_rev(str[1:]) + str[0]
    

print(fun_rev("Tanu"))



















# # reversing the string using slicing
# str = "Tanisha"
# revstr = str[::-1]
# print(revstr)

# # reversing the string using for loop
# str1 = "Tanu"
# rev = ""
# for i in range(len(str1)-1, -1, -1):
#     rev = rev + str1[i]

# print(rev)