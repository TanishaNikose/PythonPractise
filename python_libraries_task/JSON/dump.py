import json

# dict
employee = {
    'name': 'Tanisha',
    'role': 'DevOps Engineer'
}

with open('employee.json', 'w') as file: # This creates an employee.json file.
    json.dump(employee, file, indent=4)

