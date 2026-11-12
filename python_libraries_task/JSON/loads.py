import json
employee = '{"name": "Tanu", "nametype": "str"}'
response = json.loads(employee)
print(response)
print(response['name'])
print(type(response))

# Initially, employee is a string containing JSON.
# json.loads() converts that string into a Python dictionary.