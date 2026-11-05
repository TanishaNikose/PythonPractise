# 16. Create a program to check if a given string contains both uppercase and lowercase letters.

string = input("Enter string :- ")
upper = False
lower = False

for char in string:
    if char.isupper():
        upper = True
    elif char.islower():
        lower = True

if upper and lower:
    print("String contains both upper and Lower chars")
else:
    print("String does not contains Both.")