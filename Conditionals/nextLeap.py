# Create a program to check if a given year is a leap year and also determine the next leap year.

year = int(input("Enter year: "))

if year <= 0:
    print("Year cannot be zero or negative.")
else:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("The entered year is a leap year.")
    else:
        print("The entered year is not a leap year.")

    nextyear = year + 1

    while not (nextyear % 4 == 0 and (nextyear % 100 != 0 or nextyear % 400 == 0)):
        nextyear += 1

    print(f"The next leap year is {nextyear}.")
