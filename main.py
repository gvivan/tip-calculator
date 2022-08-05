#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill =  float(input("What was the total bill? $"))
tip_percent = int(input("What percentage of tip would you like to give? 10, 12, or 15?"))
num_people = int(input("How many people to split the bill?"))
bill *= 1+tip_percent/100
bill /= num_people
final_bill = "{:.2f}".format(bill)
# or use final_bill = round(bill, 2)
print(f"Each person should pay: ${final_bill} ")
