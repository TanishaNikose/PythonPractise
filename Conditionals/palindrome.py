# 9.Implement a program that checks if a string is a palindrome (reads the same forwards and backwards).

string = input("Enter the string : ")

# if string == string[::-1]:
#     print("This is a pallindrome")
# else:
#     print("Not pallindrome")


# By Loop
reverse = ''
for char in string:
    reverse = char + reverse

if reverse == string:
    print("Pallindrome")
else:
    print("Not pallindrome")