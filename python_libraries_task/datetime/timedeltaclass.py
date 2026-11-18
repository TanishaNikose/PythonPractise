# This is one of the most useful concepts for AWS automation. Timedelta represents a duration or difference between two dates/times.
    # For example:
    # - Last 24 hours.
    # - Last 7 days.
    # - Next 30 days.
    # - 5 hours from now.



from datetime import datetime, timedelta

# # substracting 24 hours
# currenttime = datetime.now()
# last24_hours = currenttime - timedelta(hours=24)
# # # last24_hours = currenttime - timedelta(hours=1) # can find for any hour.

# print('current time is ',currenttime)
# print('time before 24 hours',last24_hours)

# B. Adding 7 days 
current_time = datetime.now()
after7_days = current_time + timedelta(days=7)
print('Next week', after7_days)

# C. Different timedelta arguments
# Syntax	                       Meaning
# timedelta(days=1)	               1 day
# timedelta(hours=24)	           24 hours
# timedelta(minutes=30)	           30 minutes
# timedelta(seconds=60)	           60 seconds
# timedelta(weeks=1)	           1 week

duration = timedelta(days=2, hours=5, minutes=30)
print(duration)