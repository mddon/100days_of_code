print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip_percentage = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill?")
total_tip = (float(tip_percentage) / 100) * float(total_bill)
bill = float(total_bill) + total_tip
shared_bill = bill / float(people)
round(shared_bill, 2)
print(f"Each person should pay: ${shared_bill}")
