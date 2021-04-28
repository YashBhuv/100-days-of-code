#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

tip_calc = 1 + (tip/100)

#Each person should pay (150.00 / 5) * 1.12 = 33.6
each_pay = (bill/split) * tip_calc

#Format the result to 2 decimal places = 33.60
float_each_pay = "{:.2f}".format(each_pay)
print(f"Each person will pay: ${float_each_pay}.")