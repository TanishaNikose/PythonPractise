import json

employee = {
    'name': 'Tanu',
    'nametype': 'str'
}

response = json.dumps(employee)
print(response)
print(type(response))