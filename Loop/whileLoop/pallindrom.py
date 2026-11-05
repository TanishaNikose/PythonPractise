# 4.Create a program to check if a string is a palindrome using a while loop.

str = input("Enter Str: ").lower()
rev = str[::-1]

if str == rev:
    print("Pallindrome")
else:
    print("Not Pallindrome")
