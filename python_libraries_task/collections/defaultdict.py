# # lets first understand what is a dictionary in python. A dictionary is a collection of key-value pairs. 
# # Each key is unique and maps to a value. Dictionaries are mutable, meaning you can change their content without changing their identity.\

# employees = {
#     'name' : 'Tanisha',
#     'role' : 'DevOps Engineer'
# }

# print(employees['name'])
# print(employees['role'])
# # print(employees['salary']) # not accessible

# if  'salary' not in employees:
#     employees['salary'] = 25000

# print(employees['salary'])
# print(employees)
 
# But imagine doing this repeatedly for hundreds of keys. It becomes unnecessary extra code. This is the problem defaultdict helps solve.
# Understanding default dict

# from collections import defaultdict
# employee = defaultdict(int) # here we are passing the int as an argument to the dict. Python uses this int to generate a default value whenever we access a missing key.
# print(employee['salary']) # output is 0, Now need to understand from where this 0 came. beacuse of the argument we have give in the default dict.

# # lets understand, what doest int return 
# print(int()) # output 0
# # similarly
# print(list())
# print(str())
# print(float())
# print(set())

# here we need to understand that difault dict, calls the supplied type or callable to create a default value.
# Syntax	                  What gets created for a missing key
# defaultdict(int)	          int() → 0
# defaultdict(list)	          list() → []
# defaultdict(str)	          str() → ''
# defaultdict(float)	      float() → 0.0
# defaultdict(set)	          set() → set()


# lets understand Now that How does default dict actually work
from collections import defaultdict
count = defaultdict(int) # Here we are creating the empty dictionary.
count['AWS'] += 1 # output 1

print(count['AWS'])

# Python tries to access the AWS key.
# - Does AWS exist? No.
# - What should it do? Call int().
# - What does int() return? 0.   
# then count['AWS'] = 0 + 1 
# then count['AWS'] = 1


# That's how one line of code handles the missing key and increments its value.