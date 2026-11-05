# 24. A deployment should proceed only when tests pass and approval is received. How would you express this condition?

try:
    test = input("Did the tests pass? (True/False): ").strip().lower()
    test_approved = input("did someone approved it pass? (True/False): ").strip().lower()
    if test not in ("true", "false") or test_approved not in ("true", "false"):
        print("Please Enter True or False.")
    elif test == "true" and test_approved == "true":
        print("Deployemnt is proceeding.")
    else:
        print("Deployment not started yet. Please approve or test it.")

except ValueError:
    print("Please Enter True Or False for test passes or not.")
