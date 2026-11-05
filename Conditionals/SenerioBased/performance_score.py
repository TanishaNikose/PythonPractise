# 22. An employee receives a bonus if their performance score is above a certain threshold. How would you implement it?

try:
  performance_score = int(input("Enter score out of 100: "))
  if performance_score < 0 or performance_score > 100:
    print("Please Enter performance_score between 0 to 100")
  elif performance_score >= 80 and performance_score <= 100:
    print("Congrates, You will get the bonus of 20% of your salary.")
  elif  performance_score >= 60 and performance_score <= 80:
    print("Congrates, You will get the bonus of 10% of your salary.")
  else:
    print("Sorry! No bonus this year.")
except ValueError:
  print("Please Enter valid value.")