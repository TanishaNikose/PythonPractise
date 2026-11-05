# 14. Write a program that checks if a person is eligible for a mall discount (age <= 80 or age >=65 and a member).

age = int(input("Enter age: "))
member = input("are you a member? :- ").lower()

if age <= 0:
    print("age cant be 0 or negative.")
else:
    if age <= 80 and  age >= 65 and member == 'yes':
            print("Congrates! you are eligible for Discount coupon.")
    else:
        print("Sorry! you does not match the age criteria or membership.")