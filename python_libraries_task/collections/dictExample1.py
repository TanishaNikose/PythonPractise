# Counting repeated values

# services = ['AWS', 'Azure', 'GCP', 'AWS', 'Azure', 'AWS']


# # without difaultdict
# count = {}

# for service in services:
#     if service not in count:
#         count[service] = 0

#     count[service] += 1

# print(count)


# # with difaultdict

# from collections import defaultdict
# count = defaultdict(int)
# for service in services:
#     count[service] += 1

# print(dict(count))
# # Notice that we removed the entire if condition!







# An important concept: Does accessing a missing key modify the dictionary?

from collections import defaultdict
count = defaultdict(int)

print(count)
print(count['AWS']) 
print(count) # it atomatically created AWS key  