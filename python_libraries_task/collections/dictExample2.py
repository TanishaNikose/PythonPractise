from collections import defaultdict

employees =[
    {'name': 'Amit', 'department': 'DevOps'},
    {'name': 'Rahul', 'department': 'Development'},
    {'name': 'Priya', 'department': 'DevOps'},
    {'name': 'Sneha', 'department': 'Testing'}
]

# Your requirement is to group employees department-wise.
# It must be the output.
# {
#     'DevOps': ['Amit', 'Priya'],
#     'Development': ['Rahul'],
#     'Testing': ['Sneha']
# }

# we can achieve the output using defaultdict

grouped = defaultdict(list)
print(grouped)

for employee in employees:
    department = employee['department']
    name = employee['name']

    grouped[department].append(name)

print(dict(grouped)) # dict(grouped) converts the special defaultdict object back into a standard Python dictionary (dict) before printing it.
