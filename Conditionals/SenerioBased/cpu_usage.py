# 23. A server's CPU usage is provided as a percentage. Print Normal below 70%, Warning from 70% to below 90%, and Critical at 90% or above.

try:
    cpu_usage = int(input("Enter CPU usage in %: "))
    if cpu_usage < 0 or cpu_usage > 100:
        print("Please Enter Valid Percentage")
    elif cpu_usage < 70:
        print("Normal")
    elif cpu_usage >= 70 and cpu_usage < 90:
        print("Warning")
    else:
        print("Critical condition")  
except ValueError:
    print("Please enter valid value.")