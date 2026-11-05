# 24. Implement a program to check if a given string is a palindrome without considering spaces, punctuation, or letter casing.

str = input("Enter String :- ").lower()
cleanedString = ""

for char in str:
    if char.isalnum():
        cleanedString = cleanedString + char


reversedString = cleanedString[::-1]

if cleanedString == reversedString:
    print("pallindrome")
else:
    print("Not Paliindrome.")