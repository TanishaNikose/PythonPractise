# 6.Write a  program to determine if a given character is a vowel or a consonant using if-else.

char = input("Enter the charector:- ").lower()

# if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#     print("its a vowel")
# else:
#     print("Its a consonent")  

# python way
if char in "aeiou":
    print("vowel")
else:
    print("consonent")  