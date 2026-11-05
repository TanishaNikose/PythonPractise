# 20. Write a program using logical operators to determine if a given character is an alphabet, a digit, or a special character.


char = input("Enter char: ")

if len(char) != 1:
    print("Please enter a char")
else:
    if char.isdigit() == True:
        print("Entered char is a digit")
    elif char.isupper() == True or char.islower():
        print("Charector") 
    else:
        print("Special char") 