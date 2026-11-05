# False is treated as false.
falsy_statement = False

if falsy_statement:
    print("It is not a falsy statement.")
else:
    print("It is a falsy statement.")

# None is treated as false.
falsy_statement2 = None

if falsy_statement2:
    print("None is not a falsy statement.")
else:
    print("None is a falsy statement.")

# 0 is treated as false.
falsy_statement3 = 0

if falsy_statement3:
    print("0 is not a falsy statement.")
else:
    print("0 is a falsy statement.")

# 0.0 is treated as false.
falsy_statement4 = 0.0

if falsy_statement4:
    print("0 is not a falsy statement.")
else:
    print("0.0 is a falsy statement.")

# "" is treated as false.
falsy_statement5 = ""

if falsy_statement5:
    print(" empty string is not a falsy statement.")
else:
    print(" empty string is a falsy statement.")

# () is treated as false.
falsy_statement6 = ()

if falsy_statement6:
    print("() is not a falsy statement.")
else:
    print("() is a falsy statement.")

# {} is treated as false.
falsy_statement7 = {}

if falsy_statement7:
    print("{} is not a falsy statement.")
else:
    print("{} is a falsy statement.")

# {} is treated as false.
falsy_statement8 = {}

if falsy_statement8:
    print("{} is not a falsy statement.")
else:
    print("{} is a falsy statement.")

# set() is treated as false.
falsy_statement9 = set()

if falsy_statement9:
    print("empty set is not a falsy statement.")
else:
    print("empty set is a falsy statement.")