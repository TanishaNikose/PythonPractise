# 17. Write a Node.js program to determine if a person is a teenager (age between 13 and 19) and not a child or an adult.

age = int(input("Enter age :- "))

if age <= 0:
    print("Age cant be 0 or negative.")
else:
    if age <= 19 and age >= 13:
        print("Person is Teenager.")
    else:
        print("Person can be child or adult")