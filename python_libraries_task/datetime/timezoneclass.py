# Different countries have different timezones.

# For example:
# Location	                         Timezone

# India	                             UTC+05:30
# London (winter)	                     UTC+00:00
# New York (winter)	                 UTC-05:00

# When working with AWS, timestamps are frequently represented in UTC. So we need to understand how Python handles timezones.

# UTC stands for Coordinated Universal Time.
# It is the common reference time used globally.
# India is UTC+05:30.


# from datetime import datetime, timezone
# currenttime = datetime.now(timezone.utc)   
# print(currenttime)

# # C. What is the difference between datetime.now() and datetime.now(timezone.utc)?
# # Code                                        Meaning
# # datetime.now()	                          Current local time, without timezone information
# # datetime.now(timezone.utc)	              Current UTC time, with timezone information

# This distinction is important when comparing timestamps.



# Suppose you want to fetch CloudTrail events from the last 24 hours.

# You need:
# 1. Current UTC time.
# 2. Time 24 hours ago.
# 3. Both timestamps in UTC.

from datetime import datetime, timezone, timedelta

currenttime = datetime.now(timezone.utc)
time_24hoursago =currenttime- timedelta(hours=24)


print(currenttime)
print(time_24hoursago)

# some more concepts
# (1) strftime()
# (2) strptime()

# strftime() ---------> datetime to string

now = datetime.now()
formatted_date = now.strftime("%y-%m-%d")
print(formatted_date)

# strptimea() ----------> string to datetime 


date_string = "2026-11-16"
date_object = datetime.strptime(date_string, "%Y-%m-%d")
print(date_object)