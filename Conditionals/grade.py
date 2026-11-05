# 7.Create a program that calculates the grade of a student based on their score (A, B, C, D, or F).

score = int(input("Enter the grade"))


if score >= 0 and score <= 100:
    if score >= 95 and score <= 100:
        print("A grade")
    elif score >= 90 and score <= 94:
        print("B grade")
    elif score >= 85 and score <= 89:
        print("C grade")
    elif score >= 80 and score <= 84:
        print("D grade")
    elif score >= 75 and score <= 79:
        print("F grade")
    else:
        print("Fail")
else:
    print("please Enter the number between 0 to 100")