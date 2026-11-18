# The datetime class is used to represent a specific date and time.

from datetime import datetime
currentTime = datetime.now()
print(currentTime) # It returns the current local date and time as a datetime object.

# Example Output
# 2026-11-16 18:56:00.123456 

# Part      	Meaning
# 2026	        Year
# 11	        Month
# 16	        Day
# 18	        Hour
# 56	        Minute
# 00	        Second
# 123456	    Microseconds

# # creating the own date and time 

date = datetime(2026, 11, 17, 6, 12, 1) # datetime(year, month, day, hour, minute, second)
print(date)

# Exacting individual values

print(date.year)
print(date.month)
print(date.day)
print(date.hour)
print(date.minute)
print(date.second)