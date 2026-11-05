try:
    num = int(input("Enter the year:- "))
    if (num % 4 == 0 and num % 100 != 0 )or num % 400 == 0:
        print("Leap Year.")
    else:
        print("Not Leap Year.")
except ValueError:
    print("please enter a valid value")