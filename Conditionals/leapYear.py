# Create a program that checks if a year is a leap year (divisible by 4 but not by 100 or divisible by 400) using logical operators.

year = int(input("Enter year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Entered year is the Leap year.")
else:
    print("Entered year is not leap year.") 

# 100 isiliye liya kyuki century years leap or non-leap dono ho skte h, isliye century years ko check krne k liye 400 se divisible diya 
