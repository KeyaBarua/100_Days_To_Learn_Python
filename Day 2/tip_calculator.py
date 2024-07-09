# Greeting Message
print("Welcome to the tip calculator!")
bill = input("What was the total bill? $ ")
# Converting to float
bill = float(bill)

tip = input("How much tip would you like to give? 10, 12 or 15? ")
# Converting to int
tip = int(tip)
tip_percentage = tip / 100

people = input("How many people to split the bill? ")
# Converting to int
people = int(people)

# Calculating total bill
total_bill = bill + bill * tip_percentage
# Bill per person
# bill_per_person = round(total_bill / people, 2)

# We use the format function to format the bill with 2 decimal places because the round function
# sometimes does not format properly.
bill_per_person = "{:.2f}".format(total_bill / people)
print(f"Each person should pay: ${bill_per_person}")
