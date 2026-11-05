# 11. Write a program that determines if a given year is a century year (ends with '00').

year = int(input("Enter year :- "))

if year % 100 == 0:
    print("Century year")
else:
    print("Not a Century year")