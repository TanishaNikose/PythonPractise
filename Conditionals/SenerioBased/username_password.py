# 21. A login system asks for a username and password. How would you check whether both are correct?

username = input("Please Enter User name: ")
password = input("Please Enter password name: ")

if username == "Tanisha":
  if password == "Tanu123":
    print("Hey, You are successfully logged into your account.")
  else:
    print("Sorry!, Incorrect Password. Please try again.")
else:
  print("Incorrect Username, Please try with different.")