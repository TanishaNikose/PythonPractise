# 18. Implement a program that determines if a year is a leap year and also checks if it is a multiple of 5.

year = int(input("Enter year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
   if year % 5 == 0:
       print("Entered year is leap year and Multiple of 5.")
   else:
       print("Leap but not mul of 5")
else:
    print("not a leap year")
