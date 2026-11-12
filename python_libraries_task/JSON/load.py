import json
with open('employee.json', 'r') as file:
    response = json.load(file)

print(response)