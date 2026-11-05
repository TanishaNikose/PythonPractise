# 3.Write a program that takes a user's age as input and determines if they are eligible to vote (age >= 18).

age = int(input("Enter the Age: "))
if age == 0:
    print("Invalid Age.")
elif age >= 18:
    print("You can vote.")
else:
    print("You can't vote.")