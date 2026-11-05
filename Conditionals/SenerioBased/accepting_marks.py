# 25. How would you prevent a program from accepting marks outside the range of 0 to 100?

try:
    marks = int(input("Enter marks: ")) 
    if marks in range(0, 101):
        print("Marks Accepted.")
    else:
        print("Marks Not Accepted, Please Enter between 0 to 100.")
except ValueError:
    print("Please Enter Integer.")