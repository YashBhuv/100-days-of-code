#Day 2 Practice
#################################### EXERCISE 3 ####################################
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 
current_age = int(input("How old are you?"))
print(type(current_age))

remaining_life = int(90 - current_age)
remaining_days = int(remaining_life * 365)
remaining_weeks = int(remaining_life * 52)
remaining_months = int(remaining_life * 12)

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")



#################################### EXERCISE 2 ####################################
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
weight = input("What is your weight in 'kg' ? ")
height = input("What is your height in 'm'? ")

new_weight = float(weight)
new_height = float(height)

result = int(new_weight / (new_height ** 2))
new_result = str(result)
print("Your BMI is " + new_result)

#################################### EXERCISE 1 ####################################
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
type(two_digit_number)
value_1 = two_digit_number[0]
value_2 = two_digit_number[1]

new_value_1 = int(value_1)
new_value_2 = int(value_2)

result = print(new_value_1 + new_value_2)


######################## NOTES ##########################3
#Data types

#String > Subscripting :Pulling a character from a string 
print("Hello"[0])

#Integer (Replace ',' in large numbers with '_')
print(123+456)
print(456_1236_654)

#Float > any number with decimal 
print(3.452)

#Boolean
True
False

#TypeError
num_char = len(input("What is your name?"))

 #Converts integer to string 
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters")



