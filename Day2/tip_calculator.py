print("Welcome to the tip calculator!")
total = float(input("What was the total bill? INR"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
tip = int(input("How percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill ?"))
# 
tip_as_percent = tip / 100
total_tip_amount = total * tip_as_percent
total_amount = total + total_tip_amount

Bill_per_person = total_amount / people


print(f"Each person should pay : {round(Bill_per_person, 2)}")

