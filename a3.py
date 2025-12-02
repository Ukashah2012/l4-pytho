print("Percentage Claculator")
math = int(input("Enter your math marks:"))
science = int(input("Enter your science marks:"))
english = int(input("Enter your english marks:"))
total = math + science + english
percentage = (total / 300) * 100
print("Your total marks are:", total)
print("Your percentage is:", percentage)