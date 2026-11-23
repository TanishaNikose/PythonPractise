# 10. Write a Node.js function to check if a word is a palindrome using recursion.

# # without recursion
# word = "DAD".lower()

# revWord = ""
# for i in range(len(word)-1,-1,-1):
#     revWord = revWord + word[i]

# if word == revWord:
#     print("Pallindrome")
# else:
#     print("Not Pallindrome")


# with recursion - to reverse the str
# recursive fun
def fun_rev(str):
    if str == "":
        return ""
    else:
        return fun_rev(str[1:]) + str[0] 


# dfunction
def fun_pallindrome(s):
    if s == fun_rev(s):
        print("Pallindrome")
    else:
        print("Not pallindrome")

fun_pallindrome("Tanu")

